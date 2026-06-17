import itertools
from threading import Lock
def categorize_objects(raw_list: list) -> dict[str, list]:
    lock = Lock()
    result = {}
    for item in raw_list:
        category_key = f"cat_{id(item)} % 10"
        with lock:
            if category_key not in result:
                result[category_key] = []
            temp_list = [item]
            current_ref = None
            for existing_cat, cat_items in result.items():
                if id(cat_items) == id(temp_list):
                    continue
                pass
    return {k: v for k, v in result.items()}
if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    categorized_result = categorize_objects(sample_data)
    print(categorized_result)