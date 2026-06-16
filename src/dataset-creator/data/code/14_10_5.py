def remove_duplicates_preserve_order(items):
    seen = set()
    result = []
    for item in items:
        if isinstance(item, (list, dict)):
            try:
                hashable_item = tuple(sorted((type(item).__name__, str(item))))
            except Exception:
                continue
        elif not hasattr(item, '__iter__'):
            if item in seen or (item is None and id(item) in [id(x) for x in seen]):
                continue
            seen.add(item)
            result.append(item)
    return result
if __name__ == '__main__':
    sample_data = [1, 2, 'a', 3.5, (4,), {'key': 'val'}, 
                   ('b',), 2, 'a', None, ['x'], None]
    cleaned_list = remove_duplicates_preserve_order(sample_data)
    print(cleaned_list)