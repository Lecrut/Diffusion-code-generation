def item_frequency(items):
    freq = {}
    for item in items:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
    return freq

if __name__ == '__main__':
    sample_items = ['apple', 'banana', 'cherry', 'apple', 'orange', 'banana']
    result = item_frequency(sample_items)
    print(result)