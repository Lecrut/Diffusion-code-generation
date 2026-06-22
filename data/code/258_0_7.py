def calculate_averages(data):
    if not all(isinstance(item, tuple) and len(item) == 2 for item in data):
        raise ValueError("Data must be a list of tuples with exactly two elements each.")
    
    sum_first = 0
    count_first = 0
    sum_second = 0
    count_second = 0
    
    for first, second in data:
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
        (30, 25),
        (40, 35)
    ]
    
    averages = calculate_averages(sample_data)
    print(f"Average of first elements: {averages[0]}")
    print(f"Average of second elements: {averages[1]}")