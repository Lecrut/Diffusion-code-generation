ITEM_FREQ_DICT = {}

def count_frequencies(items):
    if not hasattr(items, '__iter__'):
        raise TypeError("Input must be iterable")
    for item in items:
        ITEM_FREQ_DICT[item] = ITEM_FREQ_DICT.get(item, 0) + 1
    return ITEM_FREQ_DICT

if __name__ == '__main__':
    sample_items = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']
    print(count_frequencies(sample_items))