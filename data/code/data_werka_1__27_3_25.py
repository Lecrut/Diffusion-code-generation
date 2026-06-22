def are_numbers_different(num1, num2):
    yield (num1 != num2)
if __name__ == '__main__':
    number1 = 42
    number2 = 42
    number3 = 7
    gen1 = are_numbers_different(number1, number2)
    gen2 = are_numbers_different(number1, number3)
    print(next(gen1))
    print(next(gen2))