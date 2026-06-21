def is_valid_iterable_of_numbers(data):
    if not data:
        return False
    for item in data:
        if not isinstance(item, (int, float)):
            return False
    return True

def find_data_span(data):
    if not is_valid_iterable_of_numbers(data):
        raise ValueError("Input must be an iterable of numbers")
    
    minimum = min(data)
    maximum = max(data)
    return maximum - minimum

if __name__ == '__main__':
    sample_data_1 = [10, 5, 20, 3, 15]
    span_1 = find_data_span(sample_data_1)
    print(f"Data: {sample_data_1}")
    print(f"Span: {span_1}")
    
    sample_data_2 = [5.5, 1.2, 8.9, 3.0]
    span_2 = find_data_span(sample_data_2)
    print(f"\nData: {sample_data_2}")
    print(f"Span: {span_2}")
    
    sample_data_3 = [42]
    span_3 = find_data_span(sample_data_3)
    print(f"\nData: {sample_data_3}")
    print(f"Span: {span_3}")