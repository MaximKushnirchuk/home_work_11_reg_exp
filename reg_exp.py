import re
from pprint import pprint

## Читаем адресную книгу в формате CSV в список contacts_list:
import csv
with open("phonebook_raw.csv") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)

# формируем список данных res_list
res_list = []
for one_man in contacts_list[1:] :
    str_ = ','.join(one_man)
    pat = re.compile(r'([А-ЯЁ][а-яё]+)\W+([А-ЯЁ][а-яё]+)\W+([А-ЯЁ]*[а-яё]*)\W*([А-ЯЁ]*[а-яё]*)\W*([c–А-ЯЁа-яё\s]*)\W*\+*(7|8*)\W*\(?(\d{,3})\)?\W*(\d{,3})\W*(\d{,2})\W*(\d{,2})\W*(доб\.\s\d{4})?\W*([^А-ЯЁа-яё\s]*)')
    sub_pat = r'\1,\2,\3,\4,\5,+7(\7)\8-\9-\10 \11,\12'
    res_sub = pat.sub(sub_pat, str_)
    res_list.append(res_sub.split(','))

# удаляем кривые телефоны из res_list
for index_man in range(len(res_list)) :
    if len(res_list[index_man][5]) < 10 :
       res_list[index_man][5] = ''

# избавляемся от дублей через словарь res_dict
res_dict = {one_man[0]:{'lastname':'', 'firstname':'', 'surname':'', 'organization':'', 'position':'', 'phone':'', 'email':''} for one_man in res_list}
for one_man in res_list :
   res_dict[one_man[0]]['lastname'] = one_man[0]
   res_dict[one_man[0]]['firstname'] = one_man[1]
   if len(res_dict[one_man[0]]['surname']) == 0 :
      res_dict[one_man[0]]['surname'] = one_man[2]
   if len(res_dict[one_man[0]]['organization']) == 0 :
      res_dict[one_man[0]]['organization'] = one_man[3]
   if len(res_dict[one_man[0]]['position']) == 0 :
      res_dict[one_man[0]]['position'] = one_man[4]
   if len(res_dict[one_man[0]]['phone']) == 0 :
      res_dict[one_man[0]]['phone'] = one_man[5]
   if len(res_dict[one_man[0]]['email']) == 0 :
      res_dict[one_man[0]]['email'] = one_man[6]

# формируем итоговый список finish_list
finish_list = list()
finish_list.append(contacts_list[0])
for one_man in res_dict.values() :
   add_list = []
   add_list.append(one_man['lastname'])
   add_list.append(one_man['firstname'])
   add_list.append(one_man['surname'])
   add_list.append(one_man['organization'])
   add_list.append(one_man['position'])
   add_list.append(one_man['phone'])
   add_list.append(one_man['email'])
   finish_list.append(add_list)


# 2. Сохраните получившиеся данные в другой файл.

with open("phonebook.csv", "w") as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(finish_list)

