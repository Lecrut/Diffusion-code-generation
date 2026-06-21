def is_dual_false(left: bool, right: bool) -> bool:
    return not (left or right)

if __name__ == '__main__':
    flag_x = False
    flag_y = False
    status = is_dual_false(flag_x, flag_y)
    print(status)