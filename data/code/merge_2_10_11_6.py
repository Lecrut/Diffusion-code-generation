import sys
def sort_dict_by_value_length(data: dict) -> list[tuple[str, str]]:
    return sorted(
        data.items(), key=lambda item: len(str(item[1])) if isinstance(item[1], (str, bytes)) else 0
    )
if __name__ == '__main__':
    sample_data = {
        "apple": "red",
        "banana": "yellow and curved",
        "cherry": "small red fruit",
        "date": "brown sweet stone fruit"
    }
    sorted_items = sort_dict_by_value_length(sample_data)
    print("Sorted items:")
    for key, value in sorted_items:
        print(f"{key}: {value}")