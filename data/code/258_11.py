def calculate_average_of_pairs(list_of_pairs):
    total_sum = 0
    total_count = 0
    for pair in list_of_pairs:
        total_sum += pair[0] + pair[1]
        total_count += 2
    if total_count == 0:
        return 0
    return total_sum / total_count
if __name__ == '__main__':
    sample_data = [[1, 2], [3, 4], [5, 6]]
    result = calculate_average_of_pairs(sample_data)
    print(result)