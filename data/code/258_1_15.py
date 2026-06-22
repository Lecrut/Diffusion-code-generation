def calculate_pair_averages(pairs):
    if not pairs:
        return {"first_average": None, "second_average": None}
    
    sum_first = 0
    sum_second = 0
    
    for pair in pairs:
        if len(pair) == 2:
            sum_first += pair[0]
            sum_second += pair[1]
    
    count = len(pairs)
    avg_first = sum_first / count if count > 0 else None
    avg_second = sum_second / count if count > 0 else None
    
    return {"first_average": avg_first, "second_average": avg_second}

if __name__ == '__main__':
    sample_data = [(10.5, 20.3), (30.7, 40.1), (50.2, 60.8)]
    result = calculate_pair_averages(sample_data)
    print(result)