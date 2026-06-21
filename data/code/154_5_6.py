def count_frequencies(data_list):
    freqs = {}
    for item in data_list:
        freqs[item] = freqs.get(item, 0) + 1
    return freqs

if __name__ == '__main__':
    sample_list = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
    result = count_frequencies(sample_list)
    print(result)