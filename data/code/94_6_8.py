import ctypes
import sys

def any_true(bool_list):
    if not bool_list:
        return False
    n = len(bool_list)
    if n == 0:
        return False
    return any(bool_list)
if __name__ == '__main__':
    sample_list_false = [False, False, False, False]
    sample_list_true = [False, False, True, False]
    sample_list_empty = []
    result_false = any_true(sample_list_false)
    result_true = any_true(sample_list_true)
    result_empty = any_true(sample_list_empty)
    print(result_false)
    print(result_true)
    print(result_empty)