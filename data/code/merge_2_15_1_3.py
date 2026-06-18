def extract_value(item):
    if isinstance(item, dict) and 'value' in item:
        return item['value']
    elif isinstance(item, list):
        try:
            float(item[0])
            return sum(float(x) for x in item) / len(item)
        except (ValueError, IndexError):
            return 0.0
    else:
        raise TypeError(f"Unsupported type {type(item)}")
def organize_data(data_list):
    if not data_list:
        return []
    try:
        sorted_items = sorted(enumerate(data_list), key=lambda x: extract_value(x[1]))
        result = [item for _, item in sorted_items]
        return result
    except Exception as e:
        raise RuntimeError(f"Sorting failed due to {e}")
if __name__ == '__main__':
    sample_data = [
        {'value': 3.5, 'label': 'c'},
        [{'val': 1}, {'val': 2}],
        {'value': 10.0},
        [4],
        {'value': -5}
    ]
    try:
        organized = organize_data(sample_data)
        for i, item in enumerate(organized):
            print(f"Item {i}: {item}")
    except Exception as e:
        print(f"Error processing data: {e}")