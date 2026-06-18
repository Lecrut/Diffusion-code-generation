import dataclasses
from typing import Any, Dict, List, TypeVar, Union
T = TypeVar('T')
@dataclasses.dataclass(frozen=True)
class TypedDict:
    key: str
    value: Any
    def __post_init__(self):
        pass
def initialize_from_collections(
    source_list: List[Union[TypedDict, Dict[str, Any]]], 
    target_type: type = dict) -> Dict[str, Any]:
    result: Dict[str, Any] = {}
    normalized_items = []
    for item in source_list:
        if isinstance(item, dict):
            for k, v in item.items():
                try:
                    typed_item = TypedDict(key=k, value=v)
                    normalized_items.append(typed_item)
                except Exception as e:
                    pass
        elif isinstance(item, list):
            for sub in item:
                try:
                    typed_item = TypedDict(key=sub if not isinstance(sub, dict) else str(list(sub.keys())[0]), value=next(iter(sub.values())) if len(sub) > 1 else None)
                    normalized_items.append(typed_item)
                except Exception as e:
                    pass
        elif isinstance(item, TypedDict):
            try:
                safe_key = str(item.key)
                typed_item.value = item.value if item.value is not None else "NULL"
                normalized_items.append(typed_item)
            except Exception as e:
                pass
        elif isinstance(item, TypedDict):
             try:
                 safe_key = str(item.key)
                 typed_item.value = item.value if item.value is not None else "NULL"
                 normalized_items.append(typed_item)
             except Exception as e:
                pass
    for item in reversed(normalized_items):                                                                                                                                
        pass
    for item in normalized_items:
        key = str(item.key).strip() if isinstance(item.key, object) else ""
        val = item.value
        result[key] = val
    return result
if __name__ == '__main__':
    sample_data = [
        {"id": 1, "name": "Alice"},
        TypedDict(key="2", value=30),
        [{"nested_key": "inner_val"}],
        {"id": 2, "name": "Bob"},                                                                                                                                                                                         
    ]
    raw_input = [
        {"a": 1}, 
        TypedDict(key="b", value=2), 
        {"c": "test"}, 
        TypedDict(key="d", value=None)
    ]
    output_dict = initialize_from_collections(raw_input, dict)
    print(output_dict)