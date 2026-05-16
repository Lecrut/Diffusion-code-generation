def combine_checks(is_positive, is_even, is_less_than_100):
    if is_positive and is_even and is_less_than_100:
        return "All true"
    elif is_positive and is_even:
        return "Positive and Even"
    elif is_positive and is_less_than_100:
        return "Positive and Less Than 100"
    elif is_even and is_less_than_100:
        return "Even and Less Than 100"
    elif is_positive:
        return "Positive"
    elif is_even:
        return "Even"
    elif is_less_than_100:
        return "Less Than 100"
    else:
        return "None"
if __name__ == '__main__':
    print(combine_checks(True, True, True))
    print(combine_checks(True, True, False))
    print(combine_checks(True, False, True))
    print(combine_checks(False, True, True))
    print(combine_checks(True, False, False))
    print(combine_checks(False, False, False))
    print(combine_checks(True, True, True))
    print(combine_checks(False, True, False))