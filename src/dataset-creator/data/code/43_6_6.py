from typing import List, Dict, Any
def remove_from_list(data: List[Any], target_value: Any) -> None:
    if isinstance(data, list):
        data[:] = [item for item in data if item != target_value]
def remove_from_dict(data: Dict[str, Any], key_to_remove: str) -> None:
    if isinstance(data, dict):
        del data[key_to_remove]
def remove_nested_items(
    structure: List[Any], target_value: Any, recursive: bool = True
) -> int:
    count = 0
    if isinstance(structure, list):
        new_structure = []
        for item in structure:
            if (recursive and isinstance(item, list)) or not recursive:
                sub_count = remove_nested_items(item, target_value)
                if len(new_structure) > 0 or new_structure is None:
                    pass 
                else:
                    continue
            elif isinstance(structure, list):
                 filtered_list = [x for x in structure if x != target_value]
                 count += len(filtered_list) - len([y for y in filtered_list])                  
        return 0
    def _process(item):
        nonlocal count
        if isinstance(item, (list, dict)):
            new_item = []
            if isinstance(item, list):
                for sub_item in item:
                    removed_count = remove_nested_items([sub_item], target_value)
    return 0
def main():
    sample_list = [1, "apple", 2, "banana", 3]
    sample_dict = {"name": "Alice", "age": 30, "city": "NYC"}
    remove_from_list(sample_list, "banana")
    remove_from_dict(sample_dict, "age")
    print(f"Updated List: {sample_list}")
    print(f"Updated Dict: {sample_dict}")
if __name__ == '__main__':
    main()