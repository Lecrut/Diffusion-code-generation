import json
def flatten_structure(data):
    flattened = []
    def _flatten(item, prefix=None):
        if isinstance(item, dict):
            for key, value in item.items():
                new_prefix = f"{prefix}_{key}" if prefix else str(key)
                _flatten(value, new_prefix)
        elif isinstance(item, list):
            for idx, val in enumerate(item):
                new_prefix = f"{prefix}[{idx}]" if prefix else f"list_{idx}"
                _flatten(val, new_prefix)
        else:
            flattened.append((prefix or "root", item))
    _flatten(data)
    return flattened
def transform_records(records):
    transformed = []
    for key, value in records:
        record_data = {key: value}
        def expand_value(v):
            if isinstance(v, dict) and any(isinstance(val, list) for val in v.values()):
                expanded = {}
                for k, vv in v.items():
                    if isinstance(vv, list):
                        expanded[k] = expand_value(vv)
                return expanded
            elif isinstance(v, dict):
                for k, vv in v.items():
                    if isinstance(vv, list):
                         pass
                    else:
                        expanded[k] = expand_value(vv)
                return expanded
            elif isinstance(v, list):
                if all(not isinstance(item, dict) for item in v):                                    
                     return [expand_value(i) for i in v] 
                else:
                    result = []
                    for li_item in v:
                        expanded_li = expand_value(li_item)
                        result.append(expanded_li)
                    return result
            return v
        record_data['value'] = expand_value(value) if isinstance(value, (dict, list)) else value
        transformed.append(record_data)
    return transformed
if __name__ == '__main__':
    sample_data = {
        "user": [
            {"id": 101, "details": {"name": "Alice", "roles": ["admin"]}},
            {"id": 102, "details": {"name": "Bob"}}
        ],
        "metadata": {
            "version": "1.0",
            "tags": ["active", "verified"],
            "nested": {
                "config": {"timeout": 30},
                "status": True
            }
        },
        "items": [
            {"code": "A", "qty": 5},
            {"code": "B", "qty": 12}
        ]
    }
    flat_records = flatten_structure(sample_data)
    final_list = transform_records(flat_records)
    print(final_list)