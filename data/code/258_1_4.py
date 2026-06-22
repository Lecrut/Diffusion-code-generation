def average_pairs(numbers):
    return [sum(pair) / 2 for pair in zip(numbers[::2], numbers[1::2])]

if __name__ == '__main__':
    sample_values = [1.5, 2.5, 3.5, 4.5, 5.5]
    print(average_pairs(sample_values))