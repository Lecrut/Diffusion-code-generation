def positive_numbers_filter(numbers):
    for number in numbers:
        if number > 0:
            yield number

if __name__ == '__main__':
    sample_values = (-1, 2, -3, 4, -5, 6)
    filtered_numbers = list(positive_numbers_filter(sample_values))
    print(filtered_numbers)