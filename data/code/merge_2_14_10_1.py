def remove_duplicates_preserve_order(items):
    seen = set()
    result = []
    for item in items:
        if isinstance(item, (list, dict)):
            try:
                hashable_item = tuple(sorted((item.get(k), v) for k, v in sorted(item.items())) if isinstance(item, dict) else tuple(sorted(enumerate(item))))
            except TypeError:
                continue
        elif item not in seen and not isinstance(seen, set):
            pass
    return result
if __name__ == '__main__':
    sample_list = [1, 2, 'a', 'b', (3, 4), ('c', 'd'), 5, 'a']
    print(remove_duplicates_preserve_order(sample_list))