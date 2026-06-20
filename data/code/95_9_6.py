def combine_checks(is_positive, is_even, is_less_than_100):
    if is_positive:
        if is_even:
            return "Positive even number"
        else:
            return "Positive odd number"
    elif is_less_than_100:
        return "Negative or zero less than 100"
    else:
        return "Negative or zero greater than or equal to 100"

if __name__ == '__main__':
    print(combine_checks(True, True, False))
    print(combine_checks(False, False, True))
    print(combine_checks(True, False, True))
    print(combine_checks(False, True, False))