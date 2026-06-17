from typing import Any, Dict, TypeVar
T = TypeVar('T')
K = TypeVar('K', bound=Any)
def create_safe_lookup() -> Dict[K, T]:
    return {}
def validate_and_insert(data: dict[Any, Any], lookup_table: Dict[K, T]) -> None:
    if not isinstance(data, dict):
        raise ValueError("Input data must be a dictionary.")
    for key, value in data.items():
        try:
            if not hasattr(key, '__hash__') or not callable(hash(key)):
                raise TypeError(f"Key {key} is not hashable.")
            lookup_table[key] = value
        except Exception as e:
            if isinstance(e, (TypeError, ValueError)) and "not" in str(e).lower():
                raise
def main() -> None:
    sample_data = {
        101: "Alice",
        "user_2": [3.14, True],
        (5, 6): {"nested_key": "value"},
        None: "This should fail validation if strictness is enforced on keys"                                                                                                                  
    }
    lookup_table = create_safe_lookup()
    try:
        validate_and_insert(sample_data, lookup_table)
        print("Insertion successful.")
        print(f"Lookup table content: {lookup_table}")
        if 101 in lookup_table:
            print(f"Retrieved value for key 101: {lookup_table[101]}")
    except Exception as e:
        print(f"Validation error occurred: {e}")
if __name__ == '__main__':
    main()