def consolidate_counts(*args):
    totals = {}
    for item in args:
        if isinstance(item, tuple) and len(item) == 2:
            key, count = item[0], int(item[1])
            totals[key] = totals.get(key, 0) + count
        elif isinstance(item, dict):
            for k, v in item.items():
                totals[k] = totals.get(k, 0) + v
    return totals
if __name__ == '__main__':
    sample_data = (
        ('apple', 5),
        ('banana', 3),
        {'orange': 2},
        ('pear', 1),
        ('apple', 4),
    )
    result = consolidate_counts(*sample_data)
    print(result)