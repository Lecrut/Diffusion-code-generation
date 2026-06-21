from collections import Counter

def validate_input(item_names):
    if not all(isinstance(item, str) for item in item_names):
        raise ValueError("All items must be strings")
    return item_names

def count_item_frequencies(item_names):
    validated_items = validate_input(item_names)
    return dict(Counter(validated_items))

if __name__ == '__main__':
    sample_items = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']
    frequencies = count_item_frequencies(sample_items)
    print(frequencies)