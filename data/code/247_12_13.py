def add_numbers(a, b):
    return a + b

if __name__ == '__main__':
    num1 = 5
    num2 = 3
    if isinstance(num1, int) and isinstance(num2, int):
        result = add_numbers(num1, num2)
        print(result)