def positive_numbers_generator(numbers_tuple):
    for number in numbers_tuple:
        if number > 0:
            yield number

if __name__ == '__main__':
    sample_values = (-1, 2, -3, 4, -5, 6)
    for positive_number in positive_numbers_generator(sample_values):
        print(positive_number)