def find_max_values(data):
    if not data:
        raise ValueError("Input dictionary cannot be empty")
    
    max_values = {}
    for column, values in data.items():
        max_values[column] = max(values)
    
    return max_values

if __name__ == '__main__':
    sample_data = {
        'column1': [10, 20, 30],
        'column2': [5.5, 6.6, 4.4],
        'column3': [-1, -2, -3]
    }
    
    max_values = find_max_values(sample_data)
    
    for column, value in max_values.items():
        print(f"Column: {column}, Max Value: {value}")