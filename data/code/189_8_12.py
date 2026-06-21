def is_valid_input(lst, predicate):
    if not isinstance(lst, list) or not callable(predicate):
        return False
    for item in lst:
        if not isinstance(item, (int, float)):
            return False
    return True

def remove_elements(lst, predicate):
    return [x for x in lst if not predicate(x)]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    predicate = lambda x: x % 2 == 0
    if is_valid_input(sample_list, predicate):
        result = remove_elements(sample_list, predicate)
        print(result)