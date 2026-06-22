def calculate_pair_averages(pairs):
    if not pairs:
        return {"first_average": None, "second_average": None}
    
    sums = [0, 0]
    count = len(pairs)
    
    for first, second in pairs:
        sums[0] += first
        sums[1] += second
    
    avgs = [sums[i] / count if count > 0 else None for i in range(2)]
    
    return {"first_average": avgs[0], "second_average": avgs[1]}

if __name__ == '__main__':
    sample_pairs = [(10, 20), (30, 40), (50, 60)]
    result = calculate_pair_averages(sample_pairs)
    print(result)