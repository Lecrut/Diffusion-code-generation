def combine_checks(is_positive, is_even, is_less_than_100):
    labels = []
    if is_positive:
        labels.append("positive")
    if is_even:
        labels.append("even")
    if is_less_than_100:
        labels.append("less than 100")
    return " | ".join(labels) if labels else "no match"

if __name__ == '__main__':
    print(combine_checks(True, True, True))
    print(combine_checks(False, False, False))
    print(combine_checks(True, False, False))