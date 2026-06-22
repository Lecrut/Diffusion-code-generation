def validate_data(data):
    if not all(isinstance(pair, tuple) and len(pair) == 2 for pair in data):
        raise ValueError("Data must be a list of tuples with exactly two elements each.")

def calculate_averages(data):
    validate_data(data)
    
    sum_first = 0
    sum_second = 0
    count = len(data)
    
    for first, second in data:
        sum_first += first
        sum_second += second
    
    average_first = sum_first / count if count > 0 else 0
    average_second = sum_second / count if count > 0 else 0
    
    return average_first, average_second

if __name__ == '__main__':
    sample_data = [
        (10, 5),
        (20, 15),
        (30, 25)
    ]
    
    averages = calculate_averages(sample_data)
    print(f"Average of first elements: {averages[0]}")
    print(f"Average of second elements: {averages[1]}")