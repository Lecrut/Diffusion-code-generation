def calculate_range(data):
    data.sort()
    return data[-1] - data[0]

if __name__ == '__main__':
    sample_data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print(calculate_range(sample_data))