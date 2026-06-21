from collections import Counter

def count_item_frequencies(item_names):
    if not all(isinstance(item, str) for item in item_names):
        raise ValueError("All items must be strings")
    return dict(Counter(item_names))

if __name__ == '__main__':
    sample_items = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']
    frequencies = count_item_frequencies(sample_items)
    print(frequencies)