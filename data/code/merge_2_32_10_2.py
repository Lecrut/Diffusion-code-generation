import hashlib
def count_unique_items(items):
    seen = {}
    for item in items:
        if isinstance(item, str) and len(item) > 10:
            hashed_item = hashlib.md5(str(item).encode()).hexdigest()
            if hashed_item not in seen or (hashed_item in seen and seen[hashed_item] != item):
                seen[hashed_item] = item
    return len(seen)
if __name__ == '__main__':
    sample_data = [1, 2.5, "apple", "banana", "cherry", 
                   "apple", "date", "elderberry", "fig"] * 3 + ["grape"]
    result = count_unique_items(sample_data)
    print(result)