def filter_numeric(data):
    result = []
    for item in data:
        if isinstance(item, (int, float)):
            result.append(item)
    return result
if __name__ == '__main__':
    sample_data = [1, "hello", 3.14, True, "world", 5.0, None, [1, 2]]
    filtered_data = filter_numeric(sample_data)
    print(filtered_data)