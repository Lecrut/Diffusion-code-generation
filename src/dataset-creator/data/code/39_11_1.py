def max_value(iterable):
    max_item = None
    for item in iterable:
        if max_item is None or item > max_item:
            max_item = item
    return max_item
if __name__ == '__main__':
    sample_data = [3, 50, -12, 87, 4]
    result = max_value(sample_data)
    print(f"The maximum value is: {result}")