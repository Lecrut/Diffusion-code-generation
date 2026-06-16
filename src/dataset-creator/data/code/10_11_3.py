import sys
def sort_dict_by_value_length(data: dict) -> list[tuple[str, int]]:
    return sorted(
        data.items(),
        key=lambda item: len(str(item[1])),
    )
if __name__ == '__main__':
    sample_data = {
        'apple': 5,
        'banana': 'fruit',
        'cherry': 3.14,
        'date': [1, 2, 3],
        'elderberry': None,
        'fig': {'nested': 'dict'},
    }
    sorted_items = sort_dict_by_value_length(sample_data)
    print("Sorted items (key: value):")
    for key, value in sorted_items:
        print(f"{key}: {value}")