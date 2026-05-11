def parse_store_data(data_list):
    result = []
    for item in data_list:
        if ':' in item:
            parts = item.split(':', 1)
            if len(parts) == 2:
                store_name = parts[0].strip()
                try:
                    age = int(parts[1].strip())
                    result.append({'store_name': store_name, 'age': age})
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