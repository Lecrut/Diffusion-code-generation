def combine_checks(is_positive, is_even, is_less_than_100):
    if is_positive:
        return 'Positive'
    elif is_even:
        return 'Even'
    elif is_less_than_100:
        return 'Less than 100'
    else:
        return 'None'
if __name__ == '__main__':
    print(combine_checks(True, False, True))
    print(combine_checks(False, True, False))
    print(combine_checks(False, False, True))
    print(combine_checks(False, False, False))