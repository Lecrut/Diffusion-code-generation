if __name__ == '__main__':
    input_data = [10.5, -2.3, 18.7, 0.0, -5.6, 30.4]
    
    if not input_data:
        range_value = None
    else:
        minimum = min(input_data)
        maximum = max(input_data)
        range_value = maximum - minimum
    
    print(f"Range of input data: {range_value}")