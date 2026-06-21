from collections import Counter

def count_items(items):
    if not all(isinstance(item, str) for item in items):
        raise ValueError("All elements in the list must be strings.")
    return dict(Counter(items))

if __name__ == '__main__':
    sample_items = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
    print(count_items(sample_items))