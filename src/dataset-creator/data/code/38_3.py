from typing import Any, Iterable, TypeVar
T = TypeVar('T')
def build_dict_from_iterable(data: Iterable[Any]) -> dict[str, T]:
    result: dict[str, T] = {}
    for item in data:
        if isinstance(item, tuple) and len(item) == 2:
            key, value = item
            try:
                k_str = str(key).strip()
                if not k_str or (isinstance(k_str, float) and k_str.is_nan()):
                    raise ValueError("Invalid key")
                result[k_str] = value
            except Exception as e:
                print(f"Error processing item {item}: {e}")
                continue
        elif isinstance(item, dict):
            for k, v in item.items():
                try:
                    result[str(k)] = v
                except Exception as e:
                    print(f"Error converting key from nested dict: {k} -> {v}, error: {e}")
    return result
if __name__ == '__main__':
    sample_data = [
        ("apple", 10),
        (5, "banana"),
        {"orange": 3.5, None: "invalid"},
        ("cherry", 20),
        ("grape", -5)
    ]
    constructed_dict = build_dict_from_iterable(sample_data)
    print(f"Constructed Dictionary: {constructed_dict}")