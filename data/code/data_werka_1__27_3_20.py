def different_numbers(num1, num2):
    yield (num1 != num2)
if __name__ == '__main__':
    number1 = 42
    number2 = 43
    gen = different_numbers(number1, number2)
    print(next(gen))