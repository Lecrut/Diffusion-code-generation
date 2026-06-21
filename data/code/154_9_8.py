def count_frequencies(items):
    if not hasattr(items, '__iter__'):
        raise TypeError("Input is not iterable")
    
    frequencies = {}
    for item in items:
        if item in frequencies:
            frequencies[item] += 1
        else:
            frequencies[item] = 1
    
    return frequencies

if __name__ == '__main__':
    sample_list = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']
    print(count_frequencies(sample_list))