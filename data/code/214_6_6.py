def find_min_value(data):
    return min(data)

if __name__ == '__main__':
    sample_data = (x for x in range(1000000))
    print(find_min_value(sample_data))