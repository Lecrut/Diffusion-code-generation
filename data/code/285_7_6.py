def compare_adjacent_pairs(numbers):
    return ['equal' if a == b else 'ascending' if a < b else 'descending' for a, b in zip(numbers, numbers[1:])]

if __name__ == '__main__':
    sample_values = [3.5, 2.1, 4.8, 4.8, 1.9]
    print(compare_adjacent_pairs(sample_values))