import sys
if __name__ == '__main__':
    input_data = [10.5, 3.2, 99.8, -5.1, 42.0]
    if not input_data:
        range_value = 0.0
    else:
        minimum = min(input_data)
        maximum = max(input_data)
        range_value = maximum - minimum
    print(range_value)