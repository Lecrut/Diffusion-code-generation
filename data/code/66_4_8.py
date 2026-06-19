def is_strictly_increasing(numbers):
    return [numbers[i] < numbers[i + 1] for i in range(len(numbers) - 1)]

if __name__ == '__main__':
    sample_values = [0.1, 0.3, 0.5, 0.7, 0.9]
    result = is_strictly_increasing(sample_values)
    print(result)