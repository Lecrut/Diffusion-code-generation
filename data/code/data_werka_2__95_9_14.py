def combine_checks(is_positive, is_even, is_less_than_100):
    flags = []
    if is_positive:
        flags.append("positive")
    if is_even:
        flags.append("even")
    if is_less_than_100:
        flags.append("less than 100")
    if not flags:
        return "none met"
    return " | ".join(flags)

if __name__ == '__main__':
    print(combine_checks(True, True, True))
    print(combine_checks(False, False, False))
    print(combine_checks(True, False, True))
    print(combine_checks(False, True, False))