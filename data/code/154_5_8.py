ITEM_COUNTS_INIT = {}

def count_item_frequencies(data):
    freqs = ITEM_COUNTS_INIT.copy()
    for item in data:
        freqs[item] = freqs.get(item, 0) + 1
    return freqs

if __name__ == '__main__':
    sample_list = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
    result = count_item_frequencies(sample_list)
    print(result)