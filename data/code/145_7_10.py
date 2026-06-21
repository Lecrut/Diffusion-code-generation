def nested_if_else_chain(flag_a, flag_b, flag_c):
    if flag_a:
        result = 'A'
        if flag_b:
            result += 'B'
            if flag_c:
                result += 'C'
        else:
            result += 'D'
    elif flag_b:
        result = 'E'
        if flag_c:
            result += 'F'
        else:
            result += 'G'
    else:
        result = 'H'
        if flag_c:
            result += 'I'
        else:
            result += 'J'
    return result
if __name__ == '__main__':
    print(nested_if_else_chain(True, True, True))
    print(nested_if_else_chain(False, True, False))
    print(nested_if_else_chain(True, False, True))
    print(nested_if_else_chain(False, False, False))