def consolidate_counts(*args):
    totals = {}
    for item in args:
        if isinstance(item, tuple) and len(item) == 2:
            key, count = item
            totals[key] = totals.get(key, 0) + count
        else:
            raise ValueError("Each argument must be a (item_name, count) tuple")
    return totals
if __name__ == '__main__':
    sample_data = [
        ('apple', 5),
        ('banana', 3),
        ('cherry', 10),
        ('apple', 2),
        ('date', 7),
    ]
    result = consolidate_counts(*sample_data)
    print(result)