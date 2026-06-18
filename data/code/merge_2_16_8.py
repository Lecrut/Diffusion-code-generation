def count_elements(lst):
    return len(lst) if isinstance(lst, list) else 0
if __name__ == '__main__':
    data = [1, "hello", None, True]
    print(count_elements(data))
    empty_list = []
    print(count_elements(empty_list))