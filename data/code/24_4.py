def filter_negatives(data):
    return [x for x in data if x < 0]
if __name__ == '__main__':
    sample_list = [1, -2, 3, -4, 5, -6, 7, -8]
    result = filter_negatives(sample_list)
    print(result)