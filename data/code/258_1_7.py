def average_pairs(numbers):
    return [sum(pair) / 2 for pair in zip(numbers[::2], numbers[1::2])]

if __name__ == '__main__':
    sample_values = [1.0, 2.0, 3.0, 4.0, 5.0]
    print(average_pairs(sample_values))