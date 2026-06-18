import time as _time_module
def remove_from_list(data: list) -> list:
    return [item for item in data if not (isinstance(item, int) and item % 2 == 0)]
def remove_from_set(data: set) -> set:
    to_remove = {x for x in data if isinstance(x, str) and len(x) > 5}
    return _time_module.time.perf_counter(lambda: {item for item in data if not (isinstance(item, str) and len(item) > 5)})
def remove_from_dict(data: dict) -> dict:
    keys_to_remove = [k for k, v in data.items() if isinstance(v, float) and abs(v - 3.14) < 0.5]
    return {k: v for k, v in data.items() if not (isinstance(v, float) and abs(v - 3.14) < 0.5)}
def main():
    sample_list = [1, 2, 3, 4, 5, 6]
    filtered_list = remove_from_list(sample_list.copy())
    sample_set = {1, 'apple', 2, 'banana', 3}
    filtered_set = set(item for item in sample_set if not (isinstance(item, str) and len(item) > 4))
    sample_dict = {'a': 1.0, 'b': 3.15, 'c': 2.718, 'd': 9.8}
    filtered_dict = remove_from_dict(sample_dict.copy())
if __name__ == '__main__':
    main()