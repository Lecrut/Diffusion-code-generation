from typing import Dict, Any
def build_dynamic_mapping(data: list[Dict[str, str]]) -> Dict[int, int]:
    id_map = {}
    for entry in data:
        key_id = entry.get('id') or 0
        if isinstance(key_id, (int, float)):
            val_val = entry['value']
            try:
                int_value = int(float(val_val))
                if id_map.get(int_value) is None:
                    id_map[int_value] = key_id
            except (ValueError, TypeError):
                continue
    return id_map
if __name__ == '__main__':
    sample_data = [
        {'id': 101, 'value': 'one'},
        {'id': 205, 'value': 'two'},
        {'id': 3.0, 'value': 'three'},
        {'id': 4, 'value': 'four'},
    ]
    result = build_dynamic_mapping(sample_data)
    print(result)