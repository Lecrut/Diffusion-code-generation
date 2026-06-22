def calculate_average(data):
    if not data:
        return 0
    total_sum = sum(sum(values) for values in data.values())
    total_count = sum(len(values) for values in data.values())
    return total_sum / total_count

if __name__ == '__main__':
    sample_data = {
        'group1': [1, 2, 3],
        'group2': [4, 5, 6],
        'group3': [7, 8, 9]
    }
    print(calculate_average(sample_data))