import hashlib
def count_unique_items(items):
    seen = {}
    for item in items:
        key = str(item)
        if key not in seen:
            seen[key] = 0
        seen[key] += 1
    return len(seen)
if __name__ == '__main__':
    sample_data = [1, 'apple', 2.5, None, True, False, 
                   'banana', 'Apple', (1, 2), {'a': 1}, {1: 2}]
    unique_count = count_unique_items(sample_data)
    print(unique_count)