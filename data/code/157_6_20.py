def is_valid_input(items):
    if not items:
        raise ValueError("Input list cannot be empty")
    return all(hasattr(item, '__lt__') for item in items)

def find_min_item(items):
    is_valid_input(items)
    return min((item for item in items))

if __name__ == '__main__':
    sample_items = [5, 3, 9, 1, 10]
    print(find_min_item(sample_items))