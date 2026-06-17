import hashlib
def count_unique_items(items):
    seen = {}
    for item in items:
        if isinstance(item, str):
            key = item.lower()
        elif hasattr(item, 'hash'):                                       
            try:
                h_key = hashlib.md5(str(item).encode()).hexdigest()
            except Exception:
                continue
        else:
            h_key = id(item)
        seen[h_key] = item
    return len(seen)
if __name__ == '__main__':
    sample_data = [1, 'apple', 2.5, 'APPLE', (3, 4), {1}, {'a'}, {1}]
    result = count_unique_items(sample_data)
    print(result)