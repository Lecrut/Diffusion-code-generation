def determine_both_false(val1, val2):
    try:
        return not bool(val1) and not bool(val2)
    except Exception as e:
        raise ValueError("Invalid input: Both arguments must be boolean-like") from e

if __name__ == '__main__':
    print(determine_both_false(0, 0))
    print(determine_both_false('hello', ''))
    print(determine_both_false(None, None))
    print(determine_both_false(True, False))