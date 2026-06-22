def find_min_value(data):
    return min(data)

if __name__ == '__main__':
    sample_data = list(range(1000000))
    print(find_min_value(sample_data))