def find_data_span(data):
    if not data:
        return None
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
    sample_data_4 = []
    span_4 = find_data_span(sample_data_4)
    print(f"\nData: {sample_data_4}")
    print(f"Span: {span_4}")