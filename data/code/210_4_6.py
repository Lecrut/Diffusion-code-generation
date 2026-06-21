def data_range(values):
    return max(values) - min(values)

if __name__ == '__main__':
    sample_values = [3, 5, 1, 8, 2]
    print(data_range(sample_values))