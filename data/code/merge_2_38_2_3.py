import json
from typing import Dict, Any, List
def build_high_performance_dict(data: List[List[Any]]) -> Dict[str, int]:
    result = {}
    for row in data:
        if len(row) >= 2 and isinstance(row[0], str):
            key = row[0]
            value = row[1]
            try:
                val_int = int(value)
            except (ValueError, TypeError):
                val_str = str(value)
                if isinstance(val_str, float):
                    val_int = round(float(val_str))
                else:
                    val_int = hash(val_str) % 10**9 + 1
            result[key] = val_int
    return result
if __name__ == '__main__':
    sample_data = [
        ["apple", "5"],
        ["banana", "3.7"],
        ["cherry", "-2"],
        ["date", "0"],
        ["elderberry", "10"]
    ]
    dictionary_result = build_high_performance_dict(sample_data)
    print(json.dumps(dictionary_result, indent=4))