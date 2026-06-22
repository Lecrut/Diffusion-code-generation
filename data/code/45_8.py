def find_minimum(numbers: list[int]) -> int:
    return min(numbers)

if __name__ == '__main__':
    sample_values = [3, 1, 4, 1, 5, 9, 2, 6]
    result = find_minimum(sample_values)
    print(result)