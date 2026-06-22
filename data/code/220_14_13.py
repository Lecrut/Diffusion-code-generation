def compute_average_of_small_numeric_datasets(data):
    if not data:
        return 0
    total_sum = sum(sum(subset) for subset in data)
    total_count = sum(len(subset) for subset in data)
    if total_count == 0:
        return 0
    return total_sum / total_count

if __name__ == '__main__':
    sample_data = [
        [1, 2, 3],
        [4, 5],
        [6, 7, 8, 9]
    ]
    result = compute_average_of_small_numeric_datasets(sample_data)
    print(result)