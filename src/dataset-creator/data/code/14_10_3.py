def remove_duplicates_preserve_order(items):
    seen = set()
    result = []
    for item in items:
        if isinstance(item, (list, dict)):
            try:
                hashable_item = tuple(sorted((k, v) for k, v in item.items()))
            except TypeError:
                continue
        elif not seen.add(str(hash(item))):
            result.append(item)
    return result
if __name__ == '__main__':
    data = [1, 2, 'a', (3, 4), 5, 'b', 'a', {6: 7}, {'8': 9}]
    cleaned_data = remove_duplicates_preserve_order(data)
    print(cleaned_data)