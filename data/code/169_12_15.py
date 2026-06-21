from collections import Counter

def calculate_item_frequencies(item_names):
    return dict(Counter(item_names))

if __name__ == '__main__':
    sample_items = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']
    frequencies = calculate_item_frequencies(sample_items)
    print(frequencies)