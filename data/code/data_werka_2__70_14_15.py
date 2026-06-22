from typing import List, Tuple, Any

def extract_boundary_items(collection: List[Any]) -> Tuple[Any, Any]:
    if not isinstance(collection, list):
        raise ValueError("Input must be a list")
    if len(collection) == 0:
        raise ValueError("List must not be empty")
    return (collection[0], collection[-1])

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    result = extract_boundary_items(sample_data)
    print(result)