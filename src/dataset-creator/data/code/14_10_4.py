def remove_duplicates_preserve_order(items):
    seen = set()
    result = []
    for item in items:
        if isinstance(item, (list, dict)):
            try:
                key = tuple(sorted((k, str(v)) for k, v in item.items()))
            except TypeError:
                continue
        else:
            key = hashable_key(item)
        if key not in seen:
            seen.add(key)
            result.append(item)
    return result
def hashable_key(obj):
    try:
        return (type(obj).__name__, obj, id(obj))
    except TypeError:
        return None
if __name__ == '__main__':
    sample_data = [1, 2, 'a', 'b', 3.5, 4, 5, 6]
    cleaned_list = remove_duplicates_preserve_order(sample_data)
    print(cleaned_list)