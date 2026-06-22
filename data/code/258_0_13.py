def calculate_averages(data):
    if not all(isinstance(pair, tuple) and len(pair) == 2 for pair in data):
        raise ValueError("All elements must be pairs of numbers")
    
    sum_first = 0
    count_first = 0
    sum_second = 0
    count_second = 0
    
    for first, second in data:
        if not (isinstance(first, (int, float)) and isinstance(second, (int, float))):
            raise ValueError("Both elements in each pair must be numbers")
        
        sum_first += first
        count_first += 1
        sum_second += second
        count_second += 1
    
    avg_first = sum_first / count_first if count_first > 0 else 0
    avg_second = sum_second / count_second if count_second > 0 else 0
    
    return avg_first, avg_second

if __name__ == '__main__':
    sample_data = [
        (10, 5),
        (20, 15),
        (30, 25)
    ]
    
    try:
        result = calculate_averages(sample_data)
        print(f"Average of first elements: {result[0]}")
        print(f"Average of second elements: {result[1]}")
    except ValueError as e:
        print(e)