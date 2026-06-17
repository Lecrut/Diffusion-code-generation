def consolidate_counts(*args):
    result = {}
    for item in args:
        if isinstance(item, tuple) and len(item) == 2:
            key, count = item[0], int(item[1])
            if key in result:
                result[key] += count
            else:
                result[key] = count
        elif isinstance(item, dict):
            for k, v in item.items():
                if k not in result:
                    result[k] = 0
                result[k] += int(v)
    return result
if __name__ == '__main__':
    sample_data = (
        ('apple', 5),
        ('banana', 3),
        {'orange': 2, 'pear': 1},
        ('grape', 4),
        ('apple', 7)
    )
    output = consolidate_counts(*sample_data)
    print(output)