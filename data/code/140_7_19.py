def filter_positive_numbers(numbers):
    for number in numbers:
        if number > 0:
            yield number

if __name__ == '__main__':
    sample_values = (-1, 2, -3, 4, 5)
    positive_numbers = filter_positive_numbers(sample_values)
    print(list(positive_numbers))