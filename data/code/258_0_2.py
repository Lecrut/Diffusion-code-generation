def average_pairs(numbers):
    return [(numbers[i] + numbers[i+1]) / 2 for i in range(0, len(numbers) - 1, 2)]

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5, 6]
    print(average_pairs(sample_values))