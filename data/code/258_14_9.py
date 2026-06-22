def average_pairs(numbers):
    return sum(a + b for a, b in zip(numbers[::2], numbers[1::2])) / len(numbers)

if __name__ == '__main__':
    sample_numbers = [10, 20, 30, 40, 50, 60]
    print(average_pairs(sample_numbers))