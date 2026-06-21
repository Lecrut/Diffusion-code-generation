import json

def extract_unique_store_names(json_string):
    try:
        data = json.loads(json_string)
        store_names = set()
        if 'stores' in data:
            for store in data['stores']:
                if 'name' in store:
                    store_names.add(store['name'])
        return sorted(list(store_names))
    except (json.JSONDecodeError, KeyError):
        return []

if __name__ == '__main__':
    sample_json = '{"stores": [{"name": "Store A"}, {"name": "Store B"}, {"name": "Store A"}]}'
    print(extract_unique_store_names(sample_json))