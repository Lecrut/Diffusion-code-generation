def combine_checks(is_positive, is_even, is_less_than_100):
    tags = []
    if is_positive:
        tags.append("positive")
    if is_even:
        tags.append("even")
    if is_less_than_100:
        tags.append("less than 100")
    if not tags:
        return "none"
    return " and ".join(tags)

if __name__ == '__main__':
    print(combine_checks(True, True, True))
    print(combine_checks(False, False, False))
    print(combine_checks(True, False, False))
    print(combine_checks(False, True, True))
    print(combine_checks(False, False, True))
    print(combine_checks(True, True, False))
    print(combine_checks(False, True, False))
    print(combine_checks(True, False, True))