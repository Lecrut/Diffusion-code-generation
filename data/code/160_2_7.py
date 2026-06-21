def validate_input(items):
    if not isinstance(items, list) or not all(isinstance(item, str) for item in items):
        raise ValueError("Input must be a list of strings")

def item_frequency(items):
    validate_input(items)
    freq = {}
    for item in items:
        freq[item] = freq.get(item, 0) + 1
    return freq

if __name__ == '__main__':
    sample_items = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
    print(item_frequency(sample_items))