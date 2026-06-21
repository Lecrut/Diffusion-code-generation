from collections import Counter

def count_frequencies(item_names):
    return dict(Counter(item_names))

if __name__ == '__main__':
    sample_items = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']
    frequencies = count_frequencies(sample_items)
    print(frequencies)