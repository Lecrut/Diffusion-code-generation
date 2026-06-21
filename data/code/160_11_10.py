def validate_items(items):
    if not isinstance(items, list):
        raise ValueError("Input must be a list of item names")
    if not all(isinstance(item, str) for item in items):
        raise ValueError("All elements in the list must be strings")

def unique_items(items):
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

if __name__ == '__main__':
    sample_items = ['apple', 'banana', 'apple', 'orange', 'banana', 'grape']
    validate_items(sample_items)
    print(unique_items(sample_items))