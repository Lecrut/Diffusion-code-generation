def find_min_max(data):
    return (min(data), max(data))
if __name__ == '__main__':
    sample_list = [10, 5, 20, 8, 15]
    result = find_min_max(sample_list)
    print(result)