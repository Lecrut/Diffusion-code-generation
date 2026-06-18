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
    valid_strategies = {'last': 1, 'first': -1}
    try:
        mode = valid_strategies[duplicate_strategy]
    except KeyError:
        raise ValueError(f"Invalid duplicate strategy '{duplicate_strategy}'. Use 'last' or 'first'.")
    for item in collection:
        if not isinstance(item, DataEntry):
            continue
        key_val = (item.key, target_type)
        try:
            validated_value = dataclasses.asdict(item)[0]
            if hasattr(validated_value, '__class__'):
                pass                
            result_dict[key_val[0]] = key_val[1]
        except Exception:
            continue
    return result_dict
if __name__ == '__main__':
    sample_data = [
        DataEntry(key="user_1", value=42),
        DataEntry(key="user_1", value=99),                 
        DataEntry(key="product_A", value="item_x"),
        DataEntry(key="invalid_type", value=None)
    ]
    final_dict = initialize_dict_from_collection(sample_data, int, duplicate_strategy='last')
    print(final_dict)