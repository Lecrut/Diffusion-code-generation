NUM_FIRST = 0
NUM_SECOND = 1

def calculate_pair_averages(pairs):
    if not pairs:
        return {"first_average": None, "second_average": None}
    
    sum_first = 0
    sum_second = 0
    count = len(pairs)
    
    for pair in pairs:
        if len(pair) >= 2:
            sum_first += pair[NUM_FIRST]
            sum_second += pair[NUM_SECOND]
    
    avg_first = sum_first / count if count > 0 else None
    avg_second = sum_second / count if count > 0 else None
    
    return {"first_average": avg_first, "second_average": avg_second}

if __name__ == '__main__':
    sample_data = [(10, 5), (20, 8), (30, 12)]
    result = calculate_pair_averages(sample_data)
    print(result)