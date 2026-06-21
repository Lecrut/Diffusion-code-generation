import array

def any_true_in_list(bool_list):
    if not bool_list:
        return False
    try:
        arr = array.array('b', bool_list)
        return bool(arr.count(1))
    except TypeError:
        return any(bool_list)

if __name__ == '__main__':
    sample_list = [False, False, False, False]
    sample_list_with_true = [False, True, False, False]
    sample_empty = []
    result_false = any_true_in_list(sample_list)
    result_true = any_true_in_list(sample_list_with_true)
    result_empty = any_true_in_list(sample_empty)
    print(result_false)
    print(result_true)
    print(result_empty)