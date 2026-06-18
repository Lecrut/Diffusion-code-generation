import dataclasses
from typing import Any, Dict, List, TypeVar, Union
T = TypeVar('T')
@dataclasses.dataclass(frozen=True)
class DataEntry:
    key: str
    value: T
def initialize_dict_from_collection(
    collection: List[Any], 
    target_type: type, 
    duplicate_strategy: str = 'last'
) -> Dict[str, Any]:
    result_dict = {}
    for item in collection:
        try:
            data_entry = target_type(key=item['key'], value=item['value'])
            key_exists = key in result_dict
            if duplicate_strategy == 'last':
                if key_exists:
                    result_dict[key] = data_entry.value
                else:
                    result_dict[data_entry.key] = data_entry.value
            elif duplicate_strategy == 'first':
                existing_value = result_dict.get(data_entry.key)
                if not isinstance(existing_value, target_type):
                    raise ValueError(f"Type mismatch for key {data_entry.key}")
            elif duplicate_strategy == 'raise':
                if key_exists:
                    raise ValueError(f"Duplicate key '{key}' found. Use a different strategy.")
        except Exception as e:
            print(f"Error processing item with key {item.get('key')}: {e}")
    return result_dict
if __name__ == '__main__':
    sample_data = [
        {'key': 'alpha', 'value': 10},
        {'key': 'beta', 'value': "text"},
        {'key': 'gamma', 'value': True},
        {'key': 'delta', 'value': None}
    ]
    try:
        final_dict = initialize_dict_from_collection(
            sample_data, 
            DataEntry, 
            duplicate_strategy='last'
        )
        print("Final Dictionary:")
        for k, v in final_dict.items():
            print(f"{k}: {v}")
    except Exception as e:
        print(f"Execution failed due to error: {e}")