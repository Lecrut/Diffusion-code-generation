def average_of_pairs(numbers):
    return sum(pair for pair in zip(numbers[::2], numbers[1::2])) / len(numbers) / 2

if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5, 6, 7, 8]
    print(average_of_pairs(sample_numbers))