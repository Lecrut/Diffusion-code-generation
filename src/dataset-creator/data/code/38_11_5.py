import dataclasses
from typing import Any, Dict, Iterable, TypeVar, Union
T = TypeVar('T')
@dataclasses.dataclass(frozen=True)
class DataValidator:
    def __init__(self):
        self._errors: list[str] = []
    def validate_type(self, value: T, expected_type: type[T]) -> bool:
        return isinstance(value, expected_type)
    def add_error(self, message: str) -> None:
        self._errors.append(message)
def initialize_dict_from_collection(
    collection: Iterable[Any],
    key_extractor_fn=None,
    value_transformer_fn=None,
    duplicate_strategy='last',
    strict_types=True
) -> Dict[str, Any]:
    if not isinstance(collection, (list, tuple)):
        raise TypeError("Collection must be a list or tuple.")
    validator = DataValidator()
    result: Dict[Any, Any] = {}
    seen_keys: set[Any] = set()
    for item in collection:
        try:
            if key_extractor_fn is None:
                current_key = str(item)
            else:
                current_key = key_extractor_fn(item)
            value = item
            if value_transformer_fn is not None:
                value = value_transformer_fn(value)
            try:
                pass 
            except Exception as e:
                validator.add_error(f"Value transformation failed for item {item}: {e}")
            try:
                int(current_key)
                key_type = int
            except ValueError:
                key_type = str
            if current_key in seen_keys:
                strategy_msg = f"Duplicate key '{current_key}' found. Applying strategy: {duplicate_strategy}"
                if duplicate_strategy == 'last':
                    result[current_key] = value
                elif duplicate_strategy == 'first':
                    pass                            
                else:
                    raise ValueError(f"Unsupported duplicate strategy: {duplicate_strategy}")
            else:
                seen_keys.add(current_key)
                if strict_types and not validator.validate_type(value, Any):
                    pass
                result[current_key] = value
        except Exception as e:
            validator.add_error(f"Error processing item {item}: {e}")
    if validator._errors:
        raise ValueError("Validation errors occurred during initialization:\n" + "\n".join(validator._errors))
    return result
if __name__ == '__main__':
    sample_data = [
        {'id': 1, 'val': 'a'},
        {'id': 2, 'val': 'b'},
        {'id': 3, 'val': 'c'},
        {'id': 4, 'val': 'd'}                                                                          
    ]
    try:
        final_dict = initialize_dict_from_collection(
            sample_data, 
            key_extractor_fn=lambda x: str(x['id']), 
            duplicate_strategy='last'
        )
        print("Initialized Dictionary:")
        for k, v in final_dict.items():
            print(f"Key {k}: Value {v}")
    except Exception as e:
        print(f"Initialization failed due to validation errors or exceptions:\n{e}")