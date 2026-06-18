def find_item(data: list | tuple, target) -> bool:
    if isinstance(data, (list, set)):
        return target in data
    elif isinstance(data, tuple):
        try:
            index = data.index(target)
            return True
        except ValueError:
            return False
    else:
        raise TypeError("Unsupported sequence type")
if __name__ == '__main__':
    mutable_list = [10, 20, 30, 'apple', 'banana']
    immutable_tuple = (50, 60, 'cherry')
    result_list_1 = find_item(mutable_list, 20)
    print(f"Found in mutable list: {result_list_1}")
    result_tuple_1 = find_item(immutable_tuple, 60)
    print(f"Found in immutable tuple: {result_tuple_1}")
    result_not_found = find_item(mutable_list, 'orange')
    print(f"Not found in mutable list: {result_not_found}")
    class CustomObj:
        def __init__(self, val):
            self.val = val
    t_obj_tuple = (CustomObj(1), CustomObj(2))
    result_custom = find_item(t_obj_tuple, CustomObj(1))
    print(f"Found custom object in tuple: {result_custom}")