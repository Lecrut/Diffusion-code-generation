def compare_booleans(a, b):
    if a == b:
        if a:
            return "True/True"
        else:
            return "False/False"
    else:
        if a:
            return "True/False"
        else:
            return "False/True"
if __name__ == '__main__':
    print(compare_booleans(True, True))
    print(compare_booleans(False, False))
    print(compare_booleans(True, False))
    print(compare_booleans(False, True))