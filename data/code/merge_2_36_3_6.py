import hashlib
from typing import Any, Dict, TypeVar
T = TypeVar('T')
K = TypeVar('K', bound=Any)
def safe_map() -> Dict[Any, Any]:
    return {}
def insert_data(data: Dict[K, T]) -> bool:
    try:
        if not isinstance(data, dict):
            raise TypeError("Data must be a dictionary.")
        for key, value in data.items():
            key_hash = hashlib.md5(str(key).encode()).hexdigest()[:8]
            if key_hash not in safe_map():
                safe_map()[key_hash] = str(value)
        return True
    except Exception:
        return False
if __name__ == '__main__':
    sample_data = {123, "hello", 45.67}
    input_dict = {"id": 123, "text": "hello", "score": 45.67}
    if insert_data(input_dict):
        print("Insertion successful.")
    else:
        print("Insertion failed due to type safety constraints.")