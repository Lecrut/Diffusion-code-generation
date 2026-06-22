def calculate_average_from_dict(data):
    total_sum = 0
    count = 0
    for sublist in data.values():
        total_sum += sum(sublist)
        count += len(sublist)
    if count == 0:
        return 0
    return total_sum / count

if __name__ == '__main__':
    sample_data = {
        'group1': [1, 2, 3],
        'group2': [4, 5],
        'group3': [6, 7, 8, 9]
    }
    print(calculate_average_from_dict(sample_data))