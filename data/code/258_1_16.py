def calculate_pair_averages(pairs):
    if not pairs:
        return {"first_average": None, "second_average": None}
    
    total_first = 0
    total_second = 0
    
    for first, second in pairs:
        total_first += first
        total_second += second
    
    count = len(pairs)
    avg_first = total_first / count if count > 0 else None
    avg_second = total_second / count if count > 0 else None
    
    return {"first_average": avg_first, "second_average": avg_second}

if __name__ == '__main__':
    sample_data = [(15.5, 25.5), (35.5, 45.5), (55.5, 65.5)]
    result = calculate_pair_averages(sample_data)
    print(result)