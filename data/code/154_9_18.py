def count_frequencies(items):
    if not hasattr(items, '__iter__'):
        raise TypeError("Input is not iterable")
    return {item: items.count(item) for item in set(items)}

if __name__ == '__main__':
    sample_items = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
    print(count_frequencies(sample_items))