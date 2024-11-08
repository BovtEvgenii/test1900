def calculate(x, y, operation):
    return x + y if operation == '+' else x - y if operation == '-' else None

def calculator():
    print("Вибери дію (+, -):")
    choice = input("Введи оператор (+ або -): ")

    if choice not in ['+', '-']:
        print("Невірний вибір!")
        return

    num1 = 10 
    num2 = 14

    result = calculate(num1, num2, choice)
    if result is not None:
        print(f"{num1} {choice} {num2} = {result}")

    calculator()