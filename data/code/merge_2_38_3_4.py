import json
from typing import Any, Iterable, Dict
def build_dict_from_iterable(data: Iterable[Any]) -> Dict[str, Any]:
    result = {}
    for item in data:
        if isinstance(item, tuple) and len(item) == 2:
            key, value = item
            try:
                k_str = str(key).strip()
                v_val = value if value is not None else "None"
                result[k_str] = json.dumps(v_val)
            except Exception:
                continue
    return result
if __name__ == '__main__':
    sample_data = [
        ("apple", 10),
        (None, "error"),
        ((3.5,), None),
        ("banana", {"nested": True}),
        ("cherry", []),
        ("date", "invalid key")
    ]
    constructed_dict = build_dict_from_iterable(sample_data)
    print(json.dumps(constructed_dict, indent=4))