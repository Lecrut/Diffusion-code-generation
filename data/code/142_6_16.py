def fast_bool_compare(a: bool, b: bool) -> bool:
    return a == b

if __name__ == '__main__':
    result = fast_bool_compare(True, True)
    print(result)
    result = fast_bool_compare(False, False)
    print(result)
    result = fast_bool_compare(True, False)
    print(result)