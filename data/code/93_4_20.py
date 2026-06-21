TRUE_FALSE_MAP = {True: "true", False: "false"}

def determine_both_false(val1, val2):
    try:
        is_false1 = not bool(val1)
    except Exception:
        is_false1 = True
    try:
        is_false2 = not bool(val2)
    except Exception:
        is_false2 = True
    return is_false1 and is_false2

if __name__ == '__main__':
    print(determine_both_false(0, 0))
    print(determine_both_false(True, False))
    print(determine_both_false([], {}))
    print(determine_both_false(None, None))
    print(determine_both_false([1], [2]))