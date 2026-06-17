def increasing_pairs_iterator(data):
    n = len(data)
    if n < 2:
        return
    for i in range(n - 1):
        yield data[i] < data[i+1]
if __name__ == '__main__':
    sample_list = [1, 3, 5, 4, 6, 6, 8]
    iterator = increasing_pairs_iterator(sample_list)
    results = list(iterator)
    print(results)