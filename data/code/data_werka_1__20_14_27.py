from typing import Any

def safe_equals(obj1: Any, obj2: Any) -> bool:
    if obj1 is None or obj2 is None:
        return False
    return obj1 == obj2

if __name__ == '__main__':
    sample_values = [None, 42, 'hello', {'key': 'value'}, (1, 2, 3)]
    for i in range(len(sample_values)):
        for j in range(len(sample_values)):
            result = safe_equals(sample_values[i], sample_values[j])
            print(f"safe_equals({sample_values[i]}, {sample_values[j]}) = {result}")