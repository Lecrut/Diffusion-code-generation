def check_and_filter(data, threshold):
    return [x for x in data if x >= threshold]
if __name__ == '__main__':
    sample_list = [10, 5, 20, 3, 15, 8, 25]
    sample_threshold = 12
    result = check_and_filter(sample_list, sample_threshold)
    print(result)