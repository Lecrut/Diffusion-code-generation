def compare_adjacent(numbers):
    result = []
    for i in range(len(numbers) - 1):
        result.append(numbers[i] < numbers[i + 1])
    return result

if __name__ == '__main__':
    sample_array = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    print(compare_adjacent(sample_array))