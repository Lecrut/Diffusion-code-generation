def calculate_average(data):
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
        'A': [1, 2, 3],
        'B': [4, 5],
        'C': [6]
    }
    print(calculate_average(sample_data))