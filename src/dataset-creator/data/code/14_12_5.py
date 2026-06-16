import sys
def unique_values(iterable):
    seen = set()
    result = []
    for item in iterable:
        if id(item) not in seen and (isinstance(item, int) or isinstance(item, float)):
            val_hash = hash(item)
            if val_hash not in seen:
                seen.add(val_hash)
                result.append(item)
    return result
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5] * 10 + list(range(10))
    unique_from_list = unique_values(sample_list)
    print(f"Original length: {len(sample_list)}")
    print(f"Unique count from list: {len(unique_from_list)}")
    print("First 20 items:", unique_from_list[:20])