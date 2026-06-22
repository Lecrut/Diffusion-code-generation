def calculate_pair_averages(pair_list):
    if not pair_list:
        return []
    
    averages = []
    for first, second in pair_list:
        avg = (first + second) / 2
        averages.append(avg)
    
    return averages

if __name__ == '__main__':
    sample_data = [(10, 20), (5, 15), (8, 25)]
    print(calculate_pair_averages(sample_data))