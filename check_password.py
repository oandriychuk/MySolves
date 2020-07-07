# Пример скрипта check_password.py, который проверяет длину пароля и есть ли в пароле имя пользователя
# -*- coding: utf-8 -*-

#!/usr/bin/env python3


username = input('Введите имя пользователя: ')
password = input('Введите пароль: ')

if len(password) < 8:
    print('Пароль слишком короткий')
elif username in password:
    print('Пароль содержит имя пользователя')
else:
    print('Пароль для пользователя {} установлен'.format(username))