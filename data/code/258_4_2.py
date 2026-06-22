def calculate_pair_averages(pair_dict):
    averages = {}
    for pair, value in pair_dict.items():
        avg = (pair[0] + pair[1]) / 2
        averages[pair] = avg
    return averages

if __name__ == '__main__':
    sample_data = {(1, 2): 3, (4, 5): 9, (6, 7): 13}
    result = calculate_pair_averages(sample_data)
    print(result)