# глобальные переменные
userChoice = 0      # переменная, которая хранит выбор пользователя	userChoice = 0
valuesArray = ['1. Вывести на экран все знаения''3. Удалить значение''4. Найти значение''5. Отсортировать значения''6. tuple''7. Введите опцию:''8. myCar''9. mySting''10. myName''11. myCity''12. умножение''13. деление''14. Вектор''15. База данных']    # Задание 1: объявить переменную, котоая будет хранить 15 значени


print('Меню:')
print('1. Вывести на экран все знаения')
print('2. Добавить значение')
print('3. Удалить значение')
print('4. Найти значение')
print('5. Отсортировать значения')
print('6. Выйти')
print('Введите опцию:')
userChoice = int(input())

# Задание 2: в цикле while создать ограничения для ввода опций таким образом, чтобы
# программа принимала только знаенчия, из меню (1-6), в остальных случаях выдвала ошибку


#Задание 3: Реализовать опцию 1 и 2 из списка меню
while userChoice != 6:
    if userChoice == 1:
        print(valuesArray)
    elif userChoice == 6:
          print(valuesArray)


print('Меню:')
print('1. Вывести на экран все знаения')
print('2. Добавить значение')
print('3. Удалить значение')
print('4. Найти значение')
print('5. Отсортировать значения')
print('6. Выйти')
print('Введите опцию:')
userChoice = int(input())

