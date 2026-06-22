import ctypes
import sys

def any_true(boolean_list):
    if not boolean_list:
        return False
    try:
        array_type = ctypes.c_bool * len(boolean_list)
        c_array = array_type(*boolean_list)
        c_pointer = ctypes.cast(c_array, ctypes.POINTER(ctypes.c_bool))
        length = len(boolean_list)
        result = ctypes.pythonapi.PyMem_Memchr(c_pointer, ctypes.c_int(1), ctypes.c_size_t(length * ctypes.sizeof(ctypes.c_bool)))
        if result:
            return True
        return False
    except Exception:
        return any(boolean_list)

if __name__ == '__main__':
    sample_list = [False, False, True, False]
    result = any_true(sample_list)
    print(result)
    
    sample_list_empty = []
    result_empty = any_true(sample_list_empty)
    print(result_empty)
    
    sample_list_all_false = [False, False, False]
    result_all_false = any_true(sample_list_all_false)
    print(result_all_false)