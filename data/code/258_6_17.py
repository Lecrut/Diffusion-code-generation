def calculate_averages(pairs):
    sum_firsts = 0
    sum_seconds = 0
    count = len(pairs)
    
    for first, second in pairs:
        sum_firsts += first
        sum_seconds += second
    
    average_firsts = sum_firsts / count
    average_seconds = sum_seconds / count
    
    return {
        "average_firsts": average_firsts,
        "average_seconds": average_seconds
    }

if __name__ == '__main__':
    sample_pairs = [
        (10, 20),
        (5, 15),
        (8, 2),
        (12, 30)
    ]
    
    result = calculate_averages(sample_pairs)
    print(result)