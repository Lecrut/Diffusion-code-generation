def find_larger_pairs(numbers):
    return [max(a, b) for a, b in zip(numbers, numbers[1:])]

if __name__ == '__main__':
    sample_values = [5, 3, 9, 2, 7, 8]
    result = find_larger_pairs(sample_values)
    print(result)