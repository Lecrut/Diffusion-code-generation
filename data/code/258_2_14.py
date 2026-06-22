def calculate_pair_averages(pairs):
    if not pairs:
        return []
    
    averages = []
    for first, second in pairs:
        average = (first + second) / 2
        averages.append(average)
    
    return averages

if __name__ == '__main__':
    sample_data = [(10, 20), (5, 15), (8, 25)]
    print(calculate_pair_averages(sample_data))