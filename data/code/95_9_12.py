def combine_checks(is_positive, is_even, is_less_than_100):
    conditions = {'positive': is_positive, 'even': is_even, 'less_than_100': is_less_than_100}
    summary = []
    for key, value in conditions.items():
        if value:
            summary.append(key.capitalize())
    return ', '.join(summary) or 'None'
if __name__ == '__main__':
    result = combine_checks(True, False, True)
    print(result)