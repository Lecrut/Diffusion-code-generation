def is_operation_permitted(data_valid, source_ok):
    return data_valid and source_ok
if __name__ == '__main__':
    print(is_operation_permitted(True, True))
    print(is_operation_permitted(False, True))
    print(is_operation_permitted(True, False))
    print(is_operation_permitted(False, False))