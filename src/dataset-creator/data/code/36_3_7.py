from typing import Any, Dict, TypeVar, Union
T = TypeVar('T')
K = TypeVar('K', bound=Union[int, float, str])
def safe_insert(data: dict) -> None:
    for k in data.keys():
        if not isinstance(k, (int, float, str)):
            raise TypeError(f"Invalid key type {type(k).__name__}. Only int, float, or str are allowed.")
    validated_data = {}
    for k, v in data.items():
        try:
            typed_key = int(k) if isinstance(k, (int, float)) else str(k)
            validated_data[typed_key] = v
        except Exception as e:
            raise TypeError(f"Failed to validate key {k}: {e}")
    for k in data.keys():
        try:
            typed_val = int(v) if isinstance(v, (int, float)) else str(v)
            validated_data[k] = typed_val
        except Exception as e:
            raise TypeError(f"Failed to validate value associated with key {k}: {e}")
    return validated_data
if __name__ == '__main__':
    sample_input = {"1": 10, "2.5": 30, "hello": [1, 2], None: "error", True: False}
    try:
        result = safe_insert(sample_input)
        print(result)
    except TypeError as e:
        print(f"Validation Error: {e}")