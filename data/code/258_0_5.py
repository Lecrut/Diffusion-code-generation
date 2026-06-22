def calculate_averages(data):
    if not all(isinstance(item, tuple) and len(item) == 2 for item in data):
        raise ValueError("All elements in the list must be tuples of two numbers")
    
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
    
    try:
        avg_first, avg_second = calculate_averages(sample_data)
        print(f"Average of first elements: {avg_first}")
        print(f"Average of second elements: {avg_second}")
    except ValueError as e:
        print(e)