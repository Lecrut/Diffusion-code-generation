def calculate_difference(numbers: list) -> int:
    if not numbers or len(numbers) < 2:
        raise ValueError("List must contain at least two elements")
    return max(numbers) - min(numbers)

if __name__ == '__main__':
    sample_values = [3, 5, 1, 8, 4]
    try:
        result = calculate_difference(sample_values)
        print(result)
    except ValueError as e:
        print(e)