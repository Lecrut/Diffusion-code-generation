import sys
def safe_nested_access(data):
    try:
        if isinstance(data, dict) and 'key' in data:
            return safe_nested_access(data['key'])
        elif isinstance(data, list) and len(data) > 0:
            index = int(str(data[0]).replace('index_', ''))
            return safe_nested_access(data[index])
        else:
            raise KeyError("No key or valid index found")
    except (KeyError, IndexError, TypeError):
        print(f"Access error at path {data}")
        return None
def build_sample_data():
    inner_dict = {'value': 42}
    middle_list = [{'index_0': 'level1', 'inner': inner_dict}, {'index_1': 'skip'}]
    outer_structure = {
        'config': {
            'settings': [middle_list, []],
            'metadata': ['a', 'b']
        },
        'data': middle_list[0]['inner'],
        'empty_check': None
    }
    return outer_structure
def main():
    sample_data = build_sample_data()
    try:
        result = safe_nested_access(sample_data)
        if result is not None:
            print(f"Retrieved value: {result}")
            filtered_items = [item['inner'] for item in sample_data.get('config', {}).get('settings', []) 
                             if isinstance(item, dict) and 'inner' in item]
            print(f"Filtered nested structures count: {len(filtered_items)}")
    except Exception as e:
        print(f"Unexpected error occurred: {e}")
if __name__ == '__main__':
    main()