def find_maximum_value(numbers: List[float]) -> float:
    if not numbers:
        raise ValueError("Input list cannot be empty")
    max_value = numbers[0]
    for number in numbers[1:]:
        if number > max_value:
            max_value = number
    return max_value

if __name__ == '__main__':
    sample_values = [3.5, 2.1, 4.8, 6.7, 2.9]
    try:
        largest_value = find_maximum_value(sample_values)
        print(f"Largest value in the list: {largest_value}")
    except ValueError as e:
        print(e)