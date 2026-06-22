def are_numbers_different(num1, num2):
    yield (num1 != num2)
if __name__ == '__main__':
    number1 = 42
    number2 = 43
    gen = are_numbers_different(number1, number2)
    print(next(gen))