def strictly_increasing_pairs(data):
    if len(data) < 2:
        return
    for i in range(len(data) - 1):
        yield data[i] < data[i+1]
if __name__ == '__main__':
    sample_list = [1, 3, 5, 4, 6, 7]
    results = list(strictly_increasing_pairs(sample_list))
    print(results)