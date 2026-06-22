def calculate_sequence_sum(numbers):
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise ValueError("All elements in the sequence must be numbers")
    return sum(numbers)

if __name__ == '__main__':
    sample_data = [1, 5, 10, 15, 20]
    try:
        result = calculate_sequence_sum(sample_data)
        print(result)
    except ValueError as e:
        print(e)