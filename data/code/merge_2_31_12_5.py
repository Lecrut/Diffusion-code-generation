from typing import Any
def map_keys_to_values(data: dict[str, list[Any]]) -> dict[str, int]:
    return {k: len(v) for k, v in data.items()}
if __name__ == '__main__':
    sample_data = {'a': [1, 2], 'b': ['x', 'y'], 'c': []}
    result = map_keys_to_values(sample_data)
    print(result)