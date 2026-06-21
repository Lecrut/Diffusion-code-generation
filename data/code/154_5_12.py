ITEM_FREQ_INITIAL = 0

def count_frequencies(data_list):
    freqs = {}
    for item in data_list:
        freqs[item] = freqs.get(item, ITEM_FREQ_INITIAL) + 1
    return freqs

if __name__ == '__main__':
    sample_list = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
    print(count_frequencies(sample_list))