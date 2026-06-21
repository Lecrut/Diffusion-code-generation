def count_frequencies(items):
    if not hasattr(items, '__iter__'):
        raise TypeError("Input must be iterable")
    
    freqs = {}
    for item in items:
        if item in freqs:
            freqs[item] += 1
        else:
            freqs[item] = 1
    
    return freqs

if __name__ == '__main__':
    sample_list = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
    print(count_frequencies(sample_list))