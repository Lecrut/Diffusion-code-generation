def check_numbers(a, b):
    return a + b > abs(a - b)

if __name__ == '__main__':
    result = check_numbers(5, 3)
    print(result)