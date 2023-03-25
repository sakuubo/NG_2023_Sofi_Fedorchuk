
num1 = float(input("Введите первое число: "))

num2 = float(input("Введите второе число: "))

operation = input("Выбрать операцию(+, -, *, /): ")

if operation == "+":
    print(num1 + num2)
elif operation == "-":
    print(num1 - num2)
elif operation == "*":
    print(num1 * num2)
elif operation == "/":
    print(num1 / num2)
else:
    print("Неверная операция")
