import sys
def sort_dict_by_value_length(data: dict) -> list[tuple]:
    return sorted(
        data.items(), 
        key=lambda item: len(item[1]) if isinstance(item[1], str) else 0,
        reverse=True
    )
if __name__ == '__main__':
    sample_data = {
        "apple": {"fruit", "red"},
        "banana": ["yellow"],
        "cherry": "delicious fruit",
        "date": [1, 2, 3],
        "elderberry": "sweet and tart"
    }
    sorted_items = sort_dict_by_value_length(sample_data)
    print("Sorted dictionary items (Key: Value):")
    for key, value in sorted_items:
        if isinstance(value, list):
            print(f"{key}: {value}")
        elif isinstance(value, set):
            print(f"{key}: {sorted(list(value))}")
        else:
            print(f"{key}: '{value}'")