def calculate_average_of_pairs(data):
    total_sum = 0
    pair_count = 0
    for pair in data:
        total_sum += sum(pair)
        pair_count += 1
    if pair_count == 0:
        return 0
    else:
        return total_sum / pair_count
if __name__ == '__main__':
    sample_data = [
        (1, 2),
        (3, 4, 5),
        (6, 7)
    ]
    average = calculate_average_of_pairs(sample_data)
    print(average)