def count_frequencies(items):
    if not hasattr(items, '__iter__'):
        raise TypeError("Input must be iterable")
    
    freq_dict = {}
    for item in items:
        freq_dict[item] = freq_dict.get(item, 0) + 1
    
    return freq_dict

if __name__ == '__main__':
    sample_items = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']
    print(count_frequencies(sample_items))