def consolidate_items(*args):
    totals = {}
    for item in args:
        if isinstance(item, tuple) and len(item) == 2:
            key, count = item[0], int(item[1])
        elif isinstance(item, dict):
            key = list(item.keys())[0]
            count = sum(item.values())
        else:
            continue
        totals[key] = totals.get(key, 0) + count
    return totals
if __name__ == '__main__':
    sample_data = (
        ('apple', 3), 
        ('banana', 5), 
        {'orange': 2}, 
        ('pear', 1), 
        ('apple', 2)
    )
    result = consolidate_items(*sample_data)
    print(result)