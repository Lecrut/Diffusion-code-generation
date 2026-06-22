def find_minimum(numbers):
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    if len(numbers) == 0:
        raise ValueError("List must not be empty")
    return min(numbers)

if __name__ == '__main__':
    sample_data = [3, 1, 4, 1, 5, 9, 2, 6]
    result = find_minimum(sample_data)
    print(result)