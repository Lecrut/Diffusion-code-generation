def nested_if_else_chain(flag1, flag2, flag3):
    if flag1:
        return "Flag 1 is True"
    elif flag2 and not flag3:
        return "Flag 2 is True and Flag 3 is False"
    else:
        return "None of the conditions met"

if __name__ == '__main__':
    print(nested_if_else_chain(True, False, True))