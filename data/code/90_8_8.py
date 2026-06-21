def check_condition(*args):
    first_half = args[:len(args) // 2]
    second_half = args[len(args) // 2:]
    left_active = False
    right_active = False
    for val in first_half:
        if val:
            left_active = True
            break
    if not left_active:
        for val in second_half:
            if val:
                right_active = True
                break
    return left_active or right_active

if __name__ == '__main__':
    vals = (False, False, False, True, False)
    status = check_condition(*vals)
    print(status)