def check_condition(*args):
    left = args[:len(args) // 2]
    right = args[len(args) // 2:]
    left_result = any(left)
    if not left_result:
        right_result = any(right)
        return right_result
    return True

if __name__ == '__main__':
    print(check_condition(False, False, True, False))
    print(check_condition(False, False, False, False))