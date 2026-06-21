from typing import Union

def check_both_false(a: Union[bool, int], b: Union[bool, int]) -> bool:
    if not isinstance(a, bool) or not isinstance(b, bool):
        raise ValueError("Inputs must be boolean")
    return a is False and b is False

if __name__ == '__main__':
    result1 = check_both_false(False, False)
    print(result1)
    result2 = check_both_false(True, False)
    print(result2)
    result3 = check_both_false(False, True)
    print(result3)
    result4 = check_both_false(True, True)
    print(result4)
    try:
        check_both_false(1, 0)
    except ValueError as e:
        print("Caught expected error:", str(e))