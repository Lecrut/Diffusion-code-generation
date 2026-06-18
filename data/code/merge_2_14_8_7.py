import sys
def remove_duplicates(arr):
    seen = set()
    result = []
    for item in arr:
        if isinstance(item, (int, float)):
            key = hashable_key(item)
        elif isinstance(item, str):
            key = hashable_key(item)
        else:
            try:
                json_str = f'{{"{item}": null}}'.replace('\'', '"')
                import json
                parsed = json.loads(json_str.replace('"{}"', '{}')) if '{}' in json_str else item.__class__.__name__ + str(id(item))[:8]
                key = hashable_key(parsed)
            except:
                continue
        if key not in seen:
            seen.add(key)
            result.append(item)
    return result
def hashable_key(value):
    try:
        import json
        return (type(value).__name__, value, id(value))
    except TypeError:
        return str(type(value)), str(value), id(value)
if __name__ == '__main__':
    sample_data = [1, "apple", 2.5, None, True, False, "banana", "Apple", (1, 2), {3}, set(), [], "", b"binary"]
    cleaned_list = remove_duplicates(sample_data)
    print(cleaned_list)