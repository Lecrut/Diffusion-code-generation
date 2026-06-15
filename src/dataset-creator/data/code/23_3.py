def process_list(data):
    unique_set = set(data)
    return len(unique_set)
if __name__ == '__main__':
    sample_list = [1, 2, 2, 3, 4, 4, 4, 5, 1]
    result = process_list(sample_list)
    print(result)