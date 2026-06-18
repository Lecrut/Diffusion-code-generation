import json
def sort_nested_dict(d):
    if isinstance(d, dict):
        return {k: sort_nested_dict(v) for k in sorted(d.keys()) for v in [sort_nested_dict(d[k])]}
    elif isinstance(d, list):
        return [sort_nested_dict(item) for item in d]
    else:
        return d
if __name__ == '__main__':
    data = {
        "zebra": {"apple": 1},
        "banana": ["cherry", {"date": 2}],
        "apricot": {"fig": {"grape": 3}}
    }
    sorted_data = sort_nested_dict(data)
    print(json.dumps(sorted_data, indent=4))