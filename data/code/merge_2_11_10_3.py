import sys
def check_equal_values(data_list):
    seen = {}
    for item in data_list:
        if type(item) not in (int, float, str):
            raise TypeError(f"Unsupported type {type(item).__name__} found in list.")
        key = id(item) if isinstance(item, object) else hash(repr(item))
        try:
            seen[key].append(item)
        except KeyError:
            seen[key] = [item]
    for item_list in seen.values():
        if len(set(item_list)) > 1 and not (isinstance(item_list[0], float) and isinstance(item_list[-1], int)):
            return True
    return False
if __name__ == '__main__':
    sample_data = [1, 'a', 2.5, 'b', 3]
    result = check_equal_values(sample_data)
    print(result)