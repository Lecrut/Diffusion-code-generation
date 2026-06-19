def different_numbers(num1, num2):
    while True:
        yield (num1 != num2)
if __name__ == '__main__':
    gen = different_numbers(3, 4)
    print(next(gen))
    print(next(gen))
    gen = different_numbers(5, 5)
    print(next(gen))
    print(next(gen))