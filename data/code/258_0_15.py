def calculate_averages(data):
    if not all(isinstance(pair, tuple) and len(pair) == 2 for pair in data):
        raise ValueError("All elements in the list must be tuples of exactly two numbers.")
    
    sum_first = sum(pair[0] for pair in data)
    sum_second = sum(pair[1] for pair in data)
    count = len(data)
    
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