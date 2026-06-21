def calculate_range(data):
    sorted_data = sorted(data)
    return sorted_data[-1] - sorted_data[0]

if __name__ == '__main__':
    sample_data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print(calculate_range(sample_data))