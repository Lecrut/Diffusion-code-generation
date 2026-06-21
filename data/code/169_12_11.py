from collections import Counter

def validate_input(item_names):
    if not isinstance(item_names, list) or not all(isinstance(item, str) for item in item_names):
        raise ValueError("Input must be a list of strings")

def count_item_frequencies(item_names):
    validate_input(item_names)
    return dict(Counter(item_names))

if __name__ == '__main__':
    sample_items = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']
    print(count_item_frequencies(sample_items))