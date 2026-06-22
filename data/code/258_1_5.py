def calculate_pair_averages(pairs):
    if not pairs:
        return {"first_average": None, "second_average": None}
    
    sums = [0, 0]
    count = len(pairs)
    
    for first, second in pairs:
        sums[0] += first
        sums[1] += second
    
    avg_first = sums[0] / count if count > 0 else None
    avg_second = sums[1] / count if count > 0 else None
    
    return {"first_average": avg_first, "second_average": avg_second}

if __name__ == '__main__':
    sample_pairs = [(10, 20), (30, 40), (50, 60)]
    result = calculate_pair_averages(sample_pairs)
    print(result)