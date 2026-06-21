def validate_input(items):
    if not all(isinstance(item, str) for item in items):
        raise ValueError("All items must be strings")

def item_frequency(items):
    freq = {}
    for item in items:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
    return freq

if __name__ == '__main__':
    sample_items = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
    validate_input(sample_items)
    print(item_frequency(sample_items))