def group_by_string_length(items):
    grouped = {}
    for item in items:
        length = len(str(item))
        if length not in grouped:
            grouped[length] = []
        grouped[length].append(item)
    return grouped

if __name__ == '__main__':
    sample_values = [123, "hello", 4567890, "world!", 1, "python"]
    result = group_by_string_length(sample_values)
    print(result)