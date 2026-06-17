from typing import Dict, List
def build_dynamic_mapping(data: List[Dict[str, int]]) -> Dict[int, str]:
    return {val: key for key, val in data}
if __name__ == '__main__':
    sample_data = [
        {"id": 101, "value": "alpha"},
        {"id": 202, "value": "beta"},
        {"id": 303, "value": "gamma"}
    ]
    result_map: Dict[int, str] = build_dynamic_mapping(sample_data)
    print(result_map)