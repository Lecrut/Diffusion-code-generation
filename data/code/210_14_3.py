def find_data_span(data):
    if not data:
        return None
    return max(data) - min(data)
if __name__ == '__main__':
    sample_data_1 = [10, 5, 20, 15]
    result_1 = find_data_span(sample_data_1)
    print(f"Data: {sample_data_1}")
    print(f"Span: {result_1}")
    sample_data_2 = [3.14, 1.618, 2.718]
    result_2 = find_data_span(sample_data_2)
    print(f"Data: {sample_data_2}")
    print(f"Span: {result_2}")
    sample_data_3 = [5]
    result_3 = find_data_span(sample_data_3)
    print(f"Data: {sample_data_3}")
    print(f"Span: {result_3}")
    sample_data_4 = []
    result_4 = find_data_span(sample_data_4)
    print(f"Data: {sample_data_4}")
    print(f"Span: {result_4}")