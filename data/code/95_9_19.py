def combine_checks(is_positive, is_even, is_less_than_100):
    if not isinstance(is_positive, bool) or not isinstance(is_even, bool) or (not isinstance(is_less_than_100, bool)):
        raise ValueError('All inputs must be boolean values.')
    summary = []
    if is_positive:
        summary.append('Positive')
    if is_even:
        summary.append('Even')
    if is_less_than_100:
        summary.append('Less than 100')
    return ', '.join(summary) or 'None'
if __name__ == '__main__':
    print(combine_checks(True, False, True))
    print(combine_checks(False, True, False))
    print(combine_checks(True, True, True))
    try:
        print(combine_checks(1, True, False))
    except ValueError as e:
        print(e)