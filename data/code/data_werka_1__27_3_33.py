def different_numbers(num1, num2):
    yield num1 != num2

if __name__ == '__main__':
    num1 = 10
    num2 = 20
    result = next(different_numbers(num1, num2))
    print(result)