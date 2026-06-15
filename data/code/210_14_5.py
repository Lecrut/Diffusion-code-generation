def find_data_span(data):
    if not data:
        return None
    minimum = min(data)
    maximum = max(data)
    return maximum - minimum
if __name__ == '__main__':
    sample_list_1 = [10, 5, 20, 15]
    sample_list_2 = [3.14, 1.618, 2.718]
    sample_list_3 = [5]
    sample_list_4 = []
    span_1 = find_data_span(sample_list_1)
    span_2 = find_data_span(sample_list_2)
    span_3 = find_data_span(sample_list_3)
    span_4 = find_data_span(sample_list_4)
    print(f"Span for {sample_list_1}: {span_1}")
    print(f"Span for {sample_list_2}: {span_2}")
    print(f"Span for {sample_list_3}: {span_3}")
    print(f"Span for {sample_list_4}: {span_4}")