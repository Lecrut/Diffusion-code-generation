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
            key = hashable_item(item)
        if key not in seen:
            seen.add(key)
            result.append(item)
    return result
def hashable_item(item):
    try:
        h = id(item)
    except Exception:
        pass
    return item
if __name__ == '__main__':
    sample_data = [1, 2, 'a', 'b', (3, 4), ('c', 'd'), 5, 6]
    print(remove_duplicates_preserve_order(sample_data))