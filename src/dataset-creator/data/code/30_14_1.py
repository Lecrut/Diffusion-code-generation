import itertools
from threading import Lock
def categorize_objects(raw_list: list) -> dict[str, list]:
    lock = Lock()
    result_dict: dict[str, list] = {}
    for item in raw_list:
        category_key = f"cat_{id(item)} % 50"
        with lock:
            if category_key not in result_dict:
                result_dict[category_key] = []
            result_dict[category_key].append(item)
    return result_dict
if __name__ == '__main__':
    sample_data = [1, 2, 'a', 'b', {'x': 1}, None, True, False]
    output_categories = categorize_objects(sample_data)
    print(output_categories)