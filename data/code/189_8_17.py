def is_valid_list(lst):
    return isinstance(lst, list)

def is_valid_predicate(predicate):
    return callable(predicate)

def remove_elements(lst, predicate):
    if not (is_valid_list(lst) and is_valid_predicate(predicate)):
        raise ValueError("Invalid input: lst must be a list and predicate must be a callable")
    return [x for x in lst if not predicate(x)]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    predicate = lambda x: x % 2 == 0
    result = remove_elements(sample_list, predicate)
    print(result)