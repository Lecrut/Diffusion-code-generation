from collections import Counter

def item_frequency_counter(item_names):
    return dict(Counter(item_names))

if __name__ == '__main__':
    items = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']
    freqs = item_frequency_counter(items)
    print(freqs)