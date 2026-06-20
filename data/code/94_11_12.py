def is_any_true(data):
    return data or any(data_list)
if __name__ == '__main__':
    print(is_any_true(True))
    print(is_any_true(False))
    print(is_any_true([True, False]))
    print(is_any_true([False, False]))