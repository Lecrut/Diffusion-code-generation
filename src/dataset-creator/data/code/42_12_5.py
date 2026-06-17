from typing import Any
def sort_dict_keys(data: dict) -> list[str]:
    return sorted(data.keys())
if __name__ == '__main__':
    sample_data = {3: 'three', 10: 'ten', 2: 'two'}
    result_keys = sort_dict_keys(sample_data)
    print(result_keys)