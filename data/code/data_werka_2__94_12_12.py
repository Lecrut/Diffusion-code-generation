TRUEY_SENTINEL = object()

def has_any_truthy_value(source):
    result = any(source)
    return result

if __name__ == '__main__':
    test_data_zero = [0, 0, 0, False, None, ""]
    test_data_one = [0, False, None, TRUEY_SENTINEL]
    test_data_empty = []
    test_data_mixed = [0, 1, 0]

    print(has_any_truthy_value(test_data_zero))
    print(has_any_truthy_value(test_data_one))
    print(has_any_truthy_value(test_data_empty))
    print(has_any_truthy_value(test_data_mixed))