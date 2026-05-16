def add_numbers(a, b):
    try:
        num1 = float(a)
        num2 = float(b)
        return num1 + num2
    except ValueError:
        return "Error: Invalid input. Please enter numeric values."
if __name__ == '__main__':
    print(add_numbers(10, 5))
    print(add_numbers("10.5", 2.5))
    print(add_numbers(10, "five"))
    print(add_numbers("hello", 5))
    print(add_numbers(3.14, 2))