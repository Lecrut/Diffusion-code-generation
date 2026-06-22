def compare_numbers(a, b):
    return f'a {">=" if a >= b else "<"} b'

if __name__ == '__main__':
    num1 = 42
    num2 = 17
    print(compare_numbers(num1, num2))