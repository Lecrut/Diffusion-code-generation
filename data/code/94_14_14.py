def is_any_true(input_bool, bool_list):
    if not isinstance(input_bool, bool) or not all(isinstance(x, bool) for x in bool_list):
        raise ValueError("Invalid input: input_bool must be a boolean and bool_list must contain only booleans")
    
    return input_bool or any(bool_list)

if __name__ == '__main__':
    print(is_any_true(True, [False, False]))
    print(is_any_true(False, [False, False]))
    print(is_any_true(False, [True, False]))
    print(is_any_true(True, [True, True]))
    print(is_any_true(False, []))