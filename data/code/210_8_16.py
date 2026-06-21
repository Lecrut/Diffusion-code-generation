def calculate_range(data):
    sorted_data = sorted(data)
    return sorted_data[-1] - sorted_data[0]

if __name__ == '__main__':
    sample_data = [5, 3, 9, 1, 7]
    print(calculate_range(sample_data))