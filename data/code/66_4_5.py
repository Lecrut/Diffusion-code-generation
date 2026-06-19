def is_strictly_increasing(numbers):
    return [numbers[i] < numbers[i + 1] for i in range(len(numbers) - 1)]

if __name__ == '__main__':
    sample_values = [1.1, 2.2, 3.3, 4.4, 5.5]
    result = is_strictly_increasing(sample_values)
    print(result)