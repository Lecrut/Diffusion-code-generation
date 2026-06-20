def combine_checks(is_positive, is_even, is_less_than_100):
    if is_positive and is_even and is_less_than_100:
        return "Number is positive, even, and less than 100."
    elif is_positive and is_even:
        return "Number is positive and even."
    elif is_positive and is_less_than_100:
        return "Number is positive and less than 100."
    elif is_even and is_less_than_100:
        return "Number is even and less than 100."
    elif is_positive:
        return "Number is positive."
    elif is_even:
        return "Number is even."
    elif is_less_than_100:
        return "Number is less than 100."
    else:
        return "Number does not meet any criteria."

if __name__ == '__main__':
    print(combine_checks(True, True, True))
    print(combine_checks(True, False, True))
    print(combine_checks(False, True, True))
    print(combine_checks(True, True, False))
    print(combine_checks(True, False, False))
    print(combine_checks(False, True, False))
    print(combine_checks(False, False, True))
    print(combine_checks(False, False, False))