def count_elements(obj):
    if isinstance(obj, list) or isinstance(obj, tuple):
        total = 0
        for item in obj:
            total += count_elements(item)
    elif isinstance(obj, dict):
        total = 0
        for _ in obj.values():
            total += count_elements(_)
    else:
        return 1
    return total
if __name__ == '__main__':
    sample_data = [1, [2, 3], {'a': 'b', 'c': ['d', '[e]']}]
    result = count_elements(sample_data)
    print(result)