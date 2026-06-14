def find_data_span(data):
    if not data:
        return None
    return max(data) - min(data)
if __name__ == '__main__':
    sample_list_1 = [10, 5, 20, 15]
    sample_list_2 = [3.14, 1.618, 2.718]
    sample_list_3 = [5]
    sample_list_4 = []
    span_1 = find_data_span(sample_list_1)
    span_2 = find_data_span(sample_list_2)
    span_3 = find_data_span(sample_list_3)
    span_4 = find_data_span(sample_list_4)
    print(f"Data: {sample_list_1}, Span: {span_1}")
    print(f"Data: {sample_list_2}, Span: {span_2}")
    print(f"Data: {sample_list_3}, Span: {span_3}")
    print(f"Data: {sample_list_4}, Span: {span_4}")