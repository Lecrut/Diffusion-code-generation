import sys
def sort_dict_by_value_length(data: dict) -> list[tuple]:
    return sorted(
        data.items(), key=lambda item: len(str(item[1])) if isinstance(item[1], str) else sys.getsizeof(item[1])
    )
if __name__ == '__main__':
    sample_data = {
        'apple': 3,
        'banana': [4, 5, 6],
        'cherry': "very long string",
        'date': None,
        'elderberry': {'nested': True},
        'fig': 123.45678901234567890,
    }
    sorted_items = sort_dict_by_value_length(sample_data)
    print("Sorted items (key: value):")
    for key, val in sorted_items:
        print(f"{key}: {val}")