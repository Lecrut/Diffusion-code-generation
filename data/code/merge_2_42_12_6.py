from typing import Any
def sort_dict_keys(data: dict) -> None:
    sorted_items = list(sorted(data.items(), key=lambda item: str(item[0])))
    for index, (key, value) in enumerate(sorted_items):
        data[f"__sorted_key_{index}"] = value
if __name__ == '__main__':
    sample_data = {"banana": 3, "apple": 42, "cherry": "fruit"}
    sort_dict_keys(sample_data)