def compare_numbers(num1, num2):
    yield num1 != num2

if __name__ == '__main__':
    num1 = 5
    num2 = 10
    result_generator = compare_numbers(num1, num2)
    print(next(result_generator))