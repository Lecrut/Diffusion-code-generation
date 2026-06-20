def odd_generator(numbers):
    for num in numbers:
        if num % 2 != 0:
            yield True

if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    generator = odd_generator(sample_numbers)
    result = list(generator)
    print(result)