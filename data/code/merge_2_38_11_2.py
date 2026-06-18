import dataclasses
from typing import Any, Dict, Iterable, TypeVar
from collections import OrderedDict
T = TypeVar('T')
@dataclasses.dataclass(frozen=True)
class TypedDict:
    _dict: dict[str, T]
    def __post_init__(self):
        if not isinstance(self._dict, dict):
            raise TypeError("TypedDict must contain a dictionary.")
def initialize_from_collection(
    collection: Iterable[Any], 
    key_type: str = "str", 
    value_type: Any = None
) -> TypedDict:
    result_dict = {}
    try:
        key_type_obj = str if key_type == "str" else int
        if isinstance(collection, (dict, list)):
            items = collection.items() if hasattr(collection, 'items') else enumerate(collection)
        elif hasattr(collection, '__iter__'):
            items = enumerate(collection)
        else:
            raise ValueError("Input must be iterable.")
        for idx, item in items:
            if isinstance(item, tuple):
                current_key, current_val = item
                if value_type and not isinstance(current_val, value_type):
                    raise TypeError(f"Value type mismatch: expected {value_type}, got {type(current_val)}")
                result_dict[current_key] = current_val
            else:
                current_key = idx
                try:
                    if isinstance(item, tuple) or len(item) == 2:
                        pass 
                    else:
                        raise ValueError("Expected iterable of tuples or list-like structures.")
                except TypeError:
                     current_key = idx
                     try:
                         if value_type and not isinstance(item, value_type):
                             raise TypeError(f"Value type mismatch: expected {value_type}, got {type(item)}")
                         result_dict[current_key] = item
                     except (TypeError, ValueError) as e:
                        pass
        return TypedDict(result_dict)
    except Exception as e:
        raise RuntimeError(f"Failed to initialize dictionary from collection: {str(e)}")
if __name__ == '__main__':
    sample_data = [
        ("Alice", 30),
        ("Bob", "Engineer"),
        (2, "Two"),                                                            
    ]
    sample_data_with_duplicates = [
        ("ID01", "Product A"),
        ("ID02", "Product B"),
        ("ID01", "Updated Product A"),                                                                                                                                        
    ]
    try:
        typed_dict_1 = initialize_from_collection(sample_data_with_duplicates, value_type=str)
        print("Initialized Dictionary:")
        for k, v in typed_dict_1._dict.items():
            print(f"{k}: {v}")
    except Exception as e:
        print(f"Error occurred during initialization: {e}")