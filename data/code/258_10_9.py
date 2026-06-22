def average_pairs(numbers):
    return sum(x + y for x, y in zip(numbers[::2], numbers[1::2])) / len(numbers)

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    print(average_pairs(sample_values))