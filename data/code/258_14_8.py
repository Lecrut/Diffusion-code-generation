def average_pairs(numbers):
    return sum(a + b for a, b in zip(numbers, numbers[1:])) / len(numbers)

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    print(average_pairs(sample_values))