def calculate_pair_averages(pairs):
    if not pairs:
        return None, None
    
    sums = [0] * 2
    for first, second in pairs:
        sums[0] += first
        sums[1] += second
    
    counts = len(pairs)
    avg_first = sums[0] / counts if counts > 0 else None
    avg_second = sums[1] / counts if counts > 0 else None
    
    return avg_first, avg_second

if __name__ == '__main__':
    sample_pairs = [(10, 20), (30, 40), (50, 60)]
    result = calculate_pair_averages(sample_pairs)
    print(result)