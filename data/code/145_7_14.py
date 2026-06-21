def nested_if_else(flag1, flag2, flag3):
    if flag1:
        result = "Flag 1 is True"
    else:
        if flag2:
            result = "Flag 2 is True"
        else:
            if flag3:
                result = "Flag 3 is True"
            else:
                result = "All flags are False"
    return result

if __name__ == '__main__':
    print(nested_if_else(True, False, False))
    print(nested_if_else(False, True, False))
    print(nested_if_else(False, False, True))
    print(nested_if_else(False, False, False))