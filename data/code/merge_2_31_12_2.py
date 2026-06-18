from typing import Dict, Any
def map_keys_to_values(data: Dict[str, int]) -> Dict[int, str]:
    return {value: key for key, value in data.items()}
if __name__ == '__main__':
    sample_data = {'a': 10, 'b': 20, 'c': 30}
    result = map_keys_to_values(sample_data)
    print(result)