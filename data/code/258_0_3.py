def average_pairs(numbers):
    return [sum(pair) / 2 for pair in zip(numbers[::2], numbers[1::2])]

if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5, 6]
    print(average_pairs(sample_numbers))