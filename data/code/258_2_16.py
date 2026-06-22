def calculate_pair_averages(pair_list):
    if not pair_list:
        return []
    
    sum_pairs = [0, 0]
    count = len(pair_list)
    
    for first, second in pair_list:
        sum_pairs[0] += first
        sum_pairs[1] += second
    
    average_pairs = [(sum_pairs[i] / count) for i in range(2)]
    return average_pairs

if __name__ == '__main__':
    sample_data = [(10, 20), (5, 15), (8, 25)]
    print(calculate_pair_averages(sample_data))