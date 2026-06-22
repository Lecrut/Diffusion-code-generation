def get_edge_elements(data):
    if not hasattr(data, '__getitem__'):
        raise ValueError("Input must be a sequence")
    if len(data) == 0:
        raise ValueError("Input must be non-empty")
    return (data[0], data[-1])

if __name__ == '__main__':
    sample_values = [42, 99, 15, 7, 3]
    edge_result = get_edge_elements(sample_values)
    print(edge_result)