def item_frequency(items):
    if not all(isinstance(item, str) for item in items):
        raise ValueError("All elements in the list must be strings")
    
    freq = {}
    for item in items:
        freq[item] = freq.get(item, 0) + 1
    return freq

if __name__ == '__main__':
    sample_items = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
    print(item_frequency(sample_items))