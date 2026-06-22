def calculate_averages(data):
    if not data or any(len(pair) != 2 for pair in data):
        raise ValueError("Data must be a list of pairs with exactly two elements each")
    
    sum_first = sum(pair[0] for pair in data)
    sum_second = sum(pair[1] for pair in data)
    count = len(data)
    
    average_first = sum_first / count if count > 0 else 0
    average_second = sum_second / count if count > 0 else 0
    
    return average_first, average_second

if __name__ == '__main__':
    sample_data = [
        (10, 5),
        (20, 15)
    ]
    try:
        result = calculate_averages(sample_data)
        print(f"Average of first elements: {result[0]}")
        print(f"Average of second elements: {result[1]}")
    except ValueError as e:
        print(e)