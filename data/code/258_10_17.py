def calculate_average_of_pairs(data):
    total_sum = sum(sum(pair) for pair in data)
    total_count = sum(len(pair) for pair in data)
    return total_sum / total_count if total_count != 0 else 0

if __name__ == '__main__':
    sample_data = [
        (1, 2),
        (3, 4, 5),
        (6, 7)
    ]
    average = calculate_average_of_pairs(sample_data)
    print(average)