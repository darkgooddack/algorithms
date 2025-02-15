# Напишите программу, которая выводит числа от 1 до 100.
# Для чисел, кратных 3, выводится слово «Fizz»
# для чисел, кратных 5, — «Buzz»
# а для чисел, кратных и 3 и 5, — «FizzBuzz»

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)