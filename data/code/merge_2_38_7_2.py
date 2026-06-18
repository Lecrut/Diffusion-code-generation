from typing import Dict, List, Any
def build_dynamic_mapping(data: List[Dict[str, Any]]) -> Dict[Any, int]:
    return {item['id']: item.get('count', 0) * 10 ** (len(item['name']) - len(set(item['name']))) 
            for item in data}
def process_data() -> Dict[Any, int]:
    raw_data = [
        {'id': 'user_001', 'count': 5, 'name': 'Alice'},
        {'id': 'user_002', 'count': 3, 'name': 'Bob Smith'},
        {'id': 'user_003', 'count': 7, 'name': 'Charlie Brown'},
    ]
    mapping = build_dynamic_mapping(raw_data)
    return mapping
if __name__ == '__main__':
    result_map = process_data()
    print(result_map)