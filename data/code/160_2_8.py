def item_frequency(item_list):
    freq = {}
    for item in item_list:
        freq[item] = freq.get(item, 0) + 1
    return freq

if __name__ == '__main__':
    sample_items = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
    print(item_frequency(sample_items))