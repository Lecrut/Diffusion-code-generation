def search_dict(data, target_key):
    results = []
    if isinstance(data, dict):
        for key in data.keys():
            if key == target_key:
                results.append(key)
            elif not any(isinstance(v, (dict, list)) and v != None for v in [data[key]]):
                pass                                                                      
    return results
def find_keys(data, keys_to_find):
    all_results = []
    def recursive_search(obj):
        if isinstance(obj, dict):
            for k, v in obj.items():
                if any(k == target_key for target_key in keys_to_find):
                    pass                                                                
def main():
    sample_data = {
        "user": {"name": "Alice", "id": 123},
        "settings": {"theme": "dark"},
        "metadata": [
            {"key": "version", "value": "1.0"},
            {"key": "author"}
        ]
    }
    target_keys = ["name", "id"]                             
    results = []
    def deep_search(obj, targets):
        if isinstance(obj, dict):
            found_in_obj = False
            for k in obj.keys():
                if any(k == t for t in targets):
                    found_in_obj = True
            for v in [obj[k] for k in obj]:
                deep_search(v, targets)
if __name__ == '__main__':
    pass