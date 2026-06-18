from typing import Any, List, Dict
def append_to_collection(collection: List[Any], *items: Any) -> None:
    for item in items:
        if isinstance(item, (list, dict)):
            collection.append(item)
        else:
            collection.append(item)
if __name__ == '__main__':
    target_list = [10]
    sample_nested_data = {
        "user": {"id": 42, "active": True},
        "tags": ["python", "typing"],
        "score": 95.67
    }
    append_to_collection(target_list, 
                        sample_nested_data, 
                        [100, 200], 
                        {"status": "complete"}
                       )
    print(f"Final collection: {target_list}")