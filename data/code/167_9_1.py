def parse_store_data(data):
    result = []
    for item in data:
        try:
            store_name, age_str = item.split(':')
            result.append({'store_name': store_name, 'age': int(age_str)})
        except ValueError:
            continue
    return result
if __name__ == '__main__':
    sample_data = [
        'StoreA:25',
        'StoreB:30',
        'StoreC:45',
        'StoreD:22',
        'InvalidEntry'
    ]
    parsed_data = parse_store_data(sample_data)
    print(parsed_data)