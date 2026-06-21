from collections import Counter

def count_items(items):
    if not all(isinstance(item, str) for item in items):
        raise ValueError("All items must be strings")
    return dict(Counter(items))

if __name__ == '__main__':
    sample_items = ["apple", "banana", "apple", "orange", "banana", "banana"]
    print(count_items(sample_items))