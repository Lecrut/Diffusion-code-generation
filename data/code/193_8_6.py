def sum_generator(numbers):
    total = 0
    for number in numbers:
        total += number
        yield total
if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5]
    gen = sum_generator(sample_numbers)
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))