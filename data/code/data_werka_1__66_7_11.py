def is_ascending(data):
    return [data[i] < data[i + 1] for i in range(len(data) - 1)]

if __name__ == '__main__':
    sample_data = [1, 3, 2, 4, 5]
    print(is_ascending(sample_data))