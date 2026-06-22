def calculate_pair_averages(data):
    if not data:
        return [0.0]
    
    averages = []
    for pair in zip(*data):
        avg = sum(pair) / len(pair)
        averages.append(avg)
    
    return averages

if __name__ == '__main__':
    sample_data = [(1, 2), (3, 4), (5, 6), (7, 8)]
    result = calculate_pair_averages(sample_data)
    print(f"{result=}")