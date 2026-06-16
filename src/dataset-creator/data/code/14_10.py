def remove_duplicates_preserve_order(data):
    seen = set()
    result = []
    for item in data:
        if isinstance(item, (str, int, float)):
            key_for_set = hashable_item(item)
        else:
            try:
                key_for_set = hash(item)
            except TypeError:
                continue
        if key_for_set not in seen:
            seen.add(key_for_set)
            result.append(item)
    return result
def hashable_item(item):
    try:
        h = hash(item)
        return (h, type(item).__name__)
    except TypeError:
        return str(item)
if __name__ == '__main__':
    sample_data = [1, 'apple', 2.5, 'banana', (3, 4), 'apple', 
                   {'a': 'b'}, 10, None, ['x'], 20]
    cleaned_list = remove_duplicates_preserve_order(sample_data)
    print(cleaned_list)