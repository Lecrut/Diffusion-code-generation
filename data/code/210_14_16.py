def calculate_range(numbers):
    if not numbers:
        return 0
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise ValueError("All elements must be numbers")
    minimum = min(numbers)
    maximum = max(numbers)
    return maximum - minimum

if __name__ == '__main__':
    sample_data_1 = [10, 5, 20, 3, 15]
    try:
        span_1 = calculate_range(sample_data_1)
        print(f"Data: {sample_data_1}")
        print(f"Span: {span_1}")
    except ValueError as e:
        print(e)

    sample_data_2 = [5.5, 1.2, 8.9, 3.0]
    try:
        span_2 = calculate_range(sample_data_2)
        print(f"\nData: {sample_data_2}")
        print(f"Span: {span_2}")
    except ValueError as e:
        print(e)

    sample_data_3 = [42]
    try:
        span_3 = calculate_range(sample_data_3)
        print(f"\nData: {sample_data_3}")
        print(f"Span: {span_3}")
    except ValueError as e:
        print(e)

    sample_data_4 = []
    try:
        span_4 = calculate_range(sample_data_4)
        print(f"\nData: {sample_data_4}")
        print(f"Span: {span_4}")
    except ValueError as e:
        print(e)