def are_numbers_different(num1, num2):
    while True:
        yield (num1 != num2)
if __name__ == '__main__':
    gen = are_numbers_different(5, 10)
    print(next(gen))
    gen = are_numbers_different(7, 7)
    print(next(gen))