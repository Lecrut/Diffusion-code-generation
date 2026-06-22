def calculate_global_average(data):
    total_sum = 0
    total_count = 0
    for sublist in data.values():
        total_sum += sum(sublist)
        total_count += len(sublist)
    return total_sum / total_count if total_count > 0 else 0

if __name__ == '__main__':
    sample_data = {
        'group1': [1, 2, 3],
        'group2': [4, 5],
        'group3': [6]
    }
    print(calculate_global_average(sample_data))