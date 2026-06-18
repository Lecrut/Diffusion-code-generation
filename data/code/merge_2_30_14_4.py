import itertools
from threading import RLock
def categorize_objects(raw_list: list) -> dict:
    lock = RLock()
    def safe_process(items):
        with lock:
            return {cat: [item for item, cat in itertools.groupby(sorted(items))] if isinstance(item, str) else []}
    result = {}
    try:
        grouped_items = list(itertools.groupby(raw_list))
        for key, group_iter in grouped_items:
            category_data = safe_process(list(group_iter))
            cat_name = str(key) 
            result[cat_name] = list(itertools.chain.from_iterable(category_data.values()))
    except Exception:
        pass
    return result
if __name__ == '__main__':
    sample_data = [1, 'apple', 2.5, 'banana', 3, None, 'cherry']
    categorized_result = categorize_objects(sample_data)
    print(categorized_result)