def safe_compare(value1, value2):

    def is_same_type(v1, v2):
        return type(v1) == type(v2)

    def handle_none(v1, v2):
        return v1 is not v2

    def compare_primitives(v1, v2):
        return v1 != v2

    def compare_lists(v1, v2):
        if len(v1) != len(v2):
            return True
        for item1, item2 in zip(v1, v2):
            if safe_compare(item1, item2):
                return True
        return False

    def compare_dicts(v1, v2):
        if v1.keys() != v2.keys():
            return True
        for key in v1:
            if safe_compare(v1[key], v2[key]):
                return True
        return False
    if not is_same_type(value1, value2):
        return True
    if value1 is None or value2 is None:
        return handle_none(value1, value2)
    if isinstance(value1, (int, float, str)):
        return compare_primitives(value1, value2)
    if isinstance(value1, list):
        return compare_lists(value1, value2)
    if isinstance(value1, dict):
        return compare_dicts(value1, value2)
    raise ValueError(f'Unsupported type: {type(value1)}')
if __name__ == '__main__':
    print(safe_compare(10, 20))
    print(safe_compare('hello', 'world'))
    print(safe_compare(None, None))
    print(safe_compare([1, 2], [1, 3]))
    print(safe_compare({'a': 1}, {'b': 2}))