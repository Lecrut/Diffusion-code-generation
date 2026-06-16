import time
from collections import OrderedDict
def sort_dict_by_value_length(data: dict) -> list[tuple]:
    return sorted(
        data.items(), key=lambda item: len(str(item[1])) if isinstance(item[1], str) else 0
    )
if __name__ == '__main__':
    sample_data = {
        'apple': 'red',
        'banana': 'yellow and curved',
        'cherry': 'small dark red fruit',
        'date': 'sweet brown seedless fruit',
        'elderberry': 'very small purple berry'
    }
    start_time = time.perf_counter()
    sorted_items = sort_dict_by_value_length(sample_data)
    end_time = time.perf_counter()
    print("Sorted items by value length:")
    for key, val in sorted_items:
        print(f"{key}: {val}")
    print(f"\nTime taken: {(end_time - start_time):.6f} seconds")