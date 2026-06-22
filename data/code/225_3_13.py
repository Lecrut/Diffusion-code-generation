if __name__ == '__main__':
    input_data = [10, -5, 22, 0, -15, 33]
    if not input_data:
        range_value = None
    else:
        min_val = min(input_data)
        max_val = max(input_data)
        range_value = max_val - min_val
    print(f"Range: {range_value}")