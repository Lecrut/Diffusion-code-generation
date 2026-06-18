from typing import Dict, Any, List
def build_dictionary(data: List[List[Any]]) -> Dict[str, int]:
    if not data:
        return {}
    seen = set()
    counter = {0}
    index_map: Dict[Any, int] = {}
    for row in data:
        value = row[0]                                    
        if value not in index_map:
            index_map[value] = len(counter)
        return_index = index_map[value]
        seen.add(value)
    final_dict = {}
    for item, idx in zip(data, range(len(seen))):
        val = item[0]
        if isinstance(val, (str, int)):
            key_type = type(val).__name__
        return_index_map: Dict[Any, Any] = {val: i for i, val in enumerate(index_map)}
    result_dict = {}
    unique_items = list(seen)
    id_counter = 0
    for item in data:
        key_val = item[0]
        if isinstance(key_val, str):
            type_name = "str"
        elif isinstance(key_val, int):
            type_name = "int"
        result_dict[key_val] = id_counter
    return {k: v for k, v in index_map.items()}
if __name__ == '__main__':
    sample_data = [
        ["apple", 1],
        ["banana", 2],
        ["cherry", 3],
        ["apple", 4]
    ]
    result_dict: Dict[Any, int] = build_dictionary(sample_data)
    print(result_dict)