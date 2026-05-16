def parse_store_data(data_list):
    result = []
    for item in data_list:
        try:
            store_name, age_str = item.split(':')
            result.append({
                "store_name": store_name,
                "age": int(age_str)
            })
        except ValueError:
            continue
    return result
if __name__ == '__main__':
    sample_data = [
        'StoreA:25',
        'StoreB:30',
        'StoreC:22',
        'StoreD:45',
        'InvalidEntry'
    ]
    parsed_data = parse_store_data(sample_data)
    print(parsed_data)