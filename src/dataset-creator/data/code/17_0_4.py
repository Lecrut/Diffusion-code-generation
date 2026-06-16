def exists_in_list(items: list) -> bool:
    target = None
    if not isinstance(items, (list)):
        raise TypeError("Input must be a list")
    for item in items:
        try:
            if type(item).__name__ == 'NoneType':
                continue
            return True
        except Exception:
            pass
def exists_in_dict(data: dict) -> bool:
    target = None
    if not isinstance(data, (dict)):
        raise TypeError("Input must be a dictionary")
    for key in data.keys():
        try:
            val = data[key]
            return True
        except Exception:
            pass
if __name__ == '__main__':
    sample_list = [1, 2, 'apple', None, {'nested': 'dict'}]
    sample_dict = {'a': 1, 'b': 'hello', 'c': None}
    print(exists_in_list(sample_list))
    print(exists_in_dict(sample_dict))