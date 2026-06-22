def compare_adjacent_elements(numbers):
    return [max(a, b) for a, b in zip(numbers, numbers[1:])]

if __name__ == '__main__':
    sample_values = [3, 5, 2, 8, 1]
    print(compare_adjacent_elements(sample_values))