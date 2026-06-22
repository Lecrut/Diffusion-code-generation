def compare_adjacent_numbers(numbers):
    for i in range(len(numbers) - 1):
        if not isinstance(numbers[i], (int, float)) or not isinstance(numbers[i + 1], (int, float)):
            raise TypeError(f"Non-numeric adjacent elements found: {numbers[i]} and {numbers[i + 1]}")
        if numbers[i] > numbers[i + 1]:
            return True
    return False

if __name__ == '__main__':
    sample_values = [3, 5, 'a', 7.2, 8]
    try:
        result = compare_adjacent_numbers(sample_values)
        print(result)
    except TypeError as e:
        print(e)