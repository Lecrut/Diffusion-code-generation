def combine_checks(is_positive, is_even, is_less_than_100):
    if not (is_positive is True or is_positive is False):
        raise ValueError("is_positive must be boolean")
    if not (is_even is True or is_even is False):
        raise ValueError("is_even must be boolean")
    if not (is_less_than_100 is True or is_less_than_100 is False):
        raise ValueError("is_less_than_100 must be boolean")

    parts = []
    if is_positive:
        parts.append("positive")
    if is_even:
        parts.append("even")
    if is_less_than_100:
        parts.append("less than 100")

    if not parts:
        return "none"
    return " and ".join(parts)

if __name__ == '__main__':
    print(combine_checks(True, True, True))
    print(combine_checks(False, False, False))
    print(combine_checks(True, False, True))
    print(combine_checks(False, True, False))