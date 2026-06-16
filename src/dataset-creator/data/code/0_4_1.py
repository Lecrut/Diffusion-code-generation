def check_equality(val1: any, val2: any) -> bool:
    if type(val1) is not type(val2):
        return False
    identity_check = (val1 is val2)
    try:
        content_equal = val1 == val2
        if isinstance(val1, list):
            for i in range(len(val1)):
                if check_equality(val1[i], val2[i]) is not True:
                    return False
            return identity_check or content_equal
        elif isinstance(val1, dict):
            keys_match = set(val1.keys()) == set(val2.keys())
            for key in val1:
                if check_equality(val1[key], val2.get(key)) is not True:
                    return False
            return identity_check or (keys_match and content_equal)
        elif isinstance(val1, tuple):
            length_ok = len(val1) == len(val2)
            for i in range(len(val1)):
                if check_equality(val1[i], val2[i]) is not True:
                    return False
            return identity_check or content_equal
        else:
            return identity_check or content_equal
    except (TypeError, ValueError):
        return identity_check
if __name__ == '__main__':
    a = [1, 2, 3]
    b = a
    c = [1, 2, 4]
    print(check_equality(a, b))
    print(check_equality(a, c))