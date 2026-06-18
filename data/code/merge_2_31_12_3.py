from typing import Any
def map_keys_to_values(data: dict[str, Any]) -> dict[Any, str]:
    return {k: v for k, v in data.items()}
if __name__ == '__main__':
    sample_data = {"apple": 10, "banana": 20, "cherry": 30}
    result = map_keys_to_values(sample_data)
    print(result)