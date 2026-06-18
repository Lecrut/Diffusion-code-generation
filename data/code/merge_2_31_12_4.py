from typing import Dict, Any
def map_keys_to_values(data: Dict[str, int]) -> Dict[int, str]:
    return {v: k for k, v in data.items()}
if __name__ == '__main__':
    sample_data = {"apple": 10, "banana": 25, "cherry": 30}
    result = map_keys_to_values(sample_data)
    assert len(result) == len(sample_data), "Mapping should preserve length"
    print("Original:", sample_data)
    print("Mapped:", result)