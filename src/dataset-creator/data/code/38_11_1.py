import dataclasses
from typing import Any, Dict, List, TypeVar, Union
T = TypeVar('T')
@dataclasses.dataclass(frozen=True)
class DataValidator:
    def validate_type(self, value: T, expected_type: type) -> bool:
        return isinstance(value, expected_type)
    def handle_duplicates(self, source: List[Dict[str, Any]], key_field: str = 'id') -> Dict[str, Any]:
        result = {}
        for item in source:
            if not self.validate_type(item.get(key_field), int):
                raise ValueError(f"Key field '{key_field}' must be an integer.")
            existing_key = item[key_field]
            current_value = dict(result)
            if existing_key in result:
                merged_result = {}
                for k, v in current_value.items():
                    merged_result[k] = v
                for k, v in item.items():
                    if k != key_field:
                        merged_result[k] = v
                result[existing_key] = merged_result
            else:
                result[existing_key] = dict(item)
        return result
def initialize_from_collection(source: List[Any], validator: DataValidator, expected_type: type) -> Dict[str, Any]:
    if validator.validate_type(source, list):
        return validator.handle_duplicates(source)
    else:
        raise TypeError(f"Source must be a {expected_type.__name__}, got {type(source).__name__}.")
if __name__ == '__main__':
    sample_data = [
        {'id': 1, 'name': 'Alice', 'age': 30},
        {'id': 2, 'name': 'Bob', 'age': 25},
        {'id': 1, 'name': 'Alice Updated', 'city': 'NYC'},                                            
    ]
    validator = DataValidator()
    try:
        final_dict = initialize_from_collection(sample_data, validator, list)
        print("Final Dictionary:")
        for k, v in final_dict.items():
            print(f"{k}: {v}")
    except Exception as e:
        print(f"Error occurred during initialization: {e}")