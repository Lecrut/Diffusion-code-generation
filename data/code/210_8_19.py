def calculate_range(data):
    data.sort()
    return data[-1] - data[0]

if __name__ == '__main__':
    sample_data = [5, 3, 9, 1, 7]
    print(calculate_range(sample_data))