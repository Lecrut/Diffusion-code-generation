def nested_if_else_chain(flag_a: bool, flag_b: bool, flag_c: bool) -> str:
    if flag_a:
        result = 'Flag A is True'
        if flag_b:
            result += ' and Flag B is True'
            if flag_c:
                result += ' and Flag C is True'
            else:
                result += ' but Flag C is False'
        else:
            result += ' but Flag B is False'
    else:
        result = 'Flag A is False'
        if flag_b:
            result += ' and Flag B is True'
            if flag_c:
                result += ' and Flag C is True'
            else:
                result += ' but Flag C is False'
        else:
            result += ' but Flag B is False'
    return result
if __name__ == '__main__':
    print(nested_if_else_chain(True, True, True))
    print(nested_if_else_chain(False, True, False))