def positive_numbers(numbers):
    for number in numbers:
        if number > 0:
            yield number

if __name__ == '__main__':
    sample_values = (-5, 3, -2, 7, 0, -1)
    for pos_num in positive_numbers(sample_values):
        print(pos_num)