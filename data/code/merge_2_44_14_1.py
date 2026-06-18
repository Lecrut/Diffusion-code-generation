import sys
def safe_nested_access(data):
    try:
        if isinstance(data, dict) and 'target' in data:
            return safe_nested_access(data['target'])
        elif isinstance(data, list) and len(data) > 0:
            item = data[0]
            if isinstance(item, (dict, list)):
                return safe_nested_access(item)
            else:
                raise ValueError("Unexpected non-iterable type in nested structure")
        else:
            return None
    except Exception as e:
        print(f"Error during access: {e}", file=sys.stderr)
        sys.exit(1)
def build_sample_data():
    inner_dict = {'value': 42, 'nested_list': [10, 20]}
    middle_level = {
        'config': inner_dict,
        'items': [{'id': 1}, {'id': 2}]
    }
    root_structure = {
        'metadata': {'source': 'demo'},
        'payload': middle_level,
        'data_list': [middle_level] * 3
    }
    return root_structure
def process_data(data):
    try:
        target_value = None
        if isinstance(data, dict) and 'payload' in data:
            payload = data['payload']
            if isinstance(payload, dict) and 'config' in payload:
                config = payload['config']
                if isinstance(config, dict):
                    target_value = safe_nested_access(data)
        processed_items = [item for item in data.get('data_list', []) 
                          if isinstance(item, dict)]
        return {
            'target_retrieved': target_value is not None,
            'items_count': len(processed_items),
            'sample_item_id': processed_items[0]['id'] if processed_items else -1
        }
    except Exception as e:
        print(f"Processing error: {e}", file=sys.stderr)
        return {'error': str(e)}
if __name__ == '__main__':
    sample_data = build_sample_data()
    result = process_data(sample_data)
    if 'target_retrieved' in result:
        print(f"Target retrieved successfully: {result['target_retrieved']}")
        print(f"Processed items count: {result['items_count']}")
        if not result.get('error'):
            sample_id = result.get('sample_item_id')
            print(f"Sample item ID found: {sample_id}")