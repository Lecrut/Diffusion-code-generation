def sum_generator(numbers):
    total = 0
    for number in numbers:
        total += number
        yield total
if __name__ == '__main__':
    sample_data = [1, 2, 3, 4, 5]
    generator = sum_generator(sample_data)
    print(next(generator))
    print(next(generator))
    print(next(generator))
    print(next(generator))
    print(next(generator))