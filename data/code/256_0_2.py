import sys
if __name__ == '__main__':
    input_data = [10.5, 3.14, 20.0, -5.5, 15.75]
    if not input_data:
        print("0.0")
    else:
        minimum = min(input_data)
        maximum = max(input_data)
        range_value = maximum - minimum
        print(range_value)