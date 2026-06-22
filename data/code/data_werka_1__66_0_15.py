def compare_adjacent(numbers):
    result = []
    for i in range(len(numbers) - 1):
        result.append(numbers[i] < numbers[i + 1])
    return result

if __name__ == '__main__':
    sample_values = [3, 5, 2, 8, 6]
    print(compare_adjacent(sample_values))