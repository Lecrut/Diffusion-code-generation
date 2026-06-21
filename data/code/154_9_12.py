def is_iterable(items):
    return hasattr(items, '__iter__')

def count_frequencies(items):
    if not is_iterable(items):
        raise TypeError("Input must be iterable")
    
    freqs = {}
    for item in items:
        freqs[item] = freqs.get(item, 0) + 1
    return freqs

if __name__ == '__main__':
    sample_list = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']
    print(count_frequencies(sample_list))