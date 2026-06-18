import sys
def sort_dict_by_value_length(data: dict) -> list[tuple[str, int]]:
    return sorted(
        data.items(),
        key=lambda item: len(item[1]),
    )
if __name__ == '__main__':
    sample_data = {
        "apple": {"fruit_type": "red", "color": 3},
        "banana": ["yellow"],
        "cherry": [4, 5],
        "date": {},
        "elderberry": [{"type": "a"}] * 100,
    }
    sorted_items = sort_dict_by_value_length(sample_data)
    print("Sorted key-value pairs:")
    for k, v in sorted_items:
        print(f"{k}: {v}")