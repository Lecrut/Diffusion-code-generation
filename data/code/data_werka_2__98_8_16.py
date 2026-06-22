def filter_records(records):
    CATEGORY_MAP = {'A': 1, 'B': 0, 'C': 0, 'D': 0}
    threshold = 100
    result = []
    for item in records:
        val = item.get('value')
        cat = item.get('category')
        is_zero = val == 0
        is_high_cat_a = val > threshold and CATEGORY_MAP.get(cat, 0) == 1
        if is_zero or is_high_cat_a:
            result.append(item)
    return result

if __name__ == '__main__':
    data = [
        {'value': 150, 'category': 'A'},
        {'value': 50, 'category': 'A'},
        {'value': 200, 'category': 'B'},
        {'value': 0, 'category': 'A'},
        {'value': 100, 'category': 'A'},
        {'value': 101, 'category': 'B'},
        {'value': 0, 'category': 'B'},
        {'value': 101, 'category': 'A'}
    ]
    print(filter_records(data))