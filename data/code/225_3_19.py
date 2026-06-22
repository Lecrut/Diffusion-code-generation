if __name__ == '__main__':
    input_data = [10.5, -5.2, 22.3, 0.7, -15.8, 33.4]
    if not input_data:
        range_value = None
    else:
        minimum = min(input_data)
        maximum = max(input_data)
        range_value = maximum - minimum
    print(f"Range: {range_value}")