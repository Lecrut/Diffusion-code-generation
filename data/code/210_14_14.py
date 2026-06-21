def validate_input(data):
    if not isinstance(data, (list, tuple)) or not all(isinstance(x, (int, float)) for x in data):
        raise ValueError("Input must be an iterable of numbers")

def calculate_range(data):
    return max(data) - min(data)

def find_data_span(data):
    validate_input(data)
    if len(data) == 1:
        return 0
    return calculate_range(data)

if __name__ == '__main__':
    sample_list_1 = [10, 5, 20, 15]
    span_1 = find_data_span(sample_list_1)
    print(f"Data: {sample_list_1}, Span: {span_1}")
    
    sample_list_2 = [3.14, 1.618, 2.718]
    span_2 = find_data_span(sample_list_2)
    print(f"Data: {sample_list_2}, Span: {span_2}")
    
    sample_list_3 = [5]
    span_3 = find_data_span(sample_list_3)
    print(f"Data: {sample_list_3}, Span: {span_3}")
    
    sample_list_4 = []
    try:
        span_4 = find_data_span(sample_list_4)
        print(f"Data: {sample_list_4}, Span: {span_4}")
    except ValueError as e:
        print(e)