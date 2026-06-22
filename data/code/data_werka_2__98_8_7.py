def process_records(records):
    CATEGORY_PRIORITY = {'A': 1, 'B': 2, 'C': 3}
    results = []
    for item in records:
        val = item.get('value')
        cat = item.get('category')
        if val is None or cat is None:
            continue
        if val == 0:
            results.append(item)
        elif cat == 'A' and val > 100:
            results.append(item)
    return results

if __name__ == '__main__':
    input_data = [
        {'value': 101, 'category': 'A'},
        {'value': 50, 'category': 'A'},
        {'value': 0, 'category': 'B'},
        {'value': 200, 'category': 'A'},
        {'value': 100, 'category': 'A'},
        {'value': 0, 'category': 'A'},
        {'value': 10, 'category': 'C'}
    ]
    output = process_records(input_data)
    print(output)