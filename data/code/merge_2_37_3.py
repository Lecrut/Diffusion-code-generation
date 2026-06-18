def consolidate_items(*args):
    totals = {}
    for item in args:
        if isinstance(item, tuple) and len(item) == 2:
            key, count = item[0], int(item[1])
            totals[key] = totals.get(key, 0) + count
        elif isinstance(item, dict):
            for k, v in item.items():
                totals[k] = totals.get(k, 0) + int(v) if not isinstance(v, (int, float)) else int(v)
    return totals
if __name__ == '__main__':
    sample_data = [
        ('apple', 5),
        ('banana', 3),
        {'orange': 2},
        ('pear', 10),
        ('apple', 7)
    ]
    result = consolidate_items(*sample_data)
    print(result)