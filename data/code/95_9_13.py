def combine_checks(is_positive, is_even, is_less_than_100):
    labels = []
    if is_positive:
        labels.append("positive")
    if is_even:
        labels.append("even")
    if is_less_than_100:
        labels.append("less than 100")
    if not labels:
        return "no match"
    return " | ".join(labels)

if __name__ == '__main__':
    val1 = combine_checks(False, True, True)
    print(val1)
    val2 = combine_checks(True, False, False)
    print(val2)
    val3 = combine_checks(True, True, True)
    print(val3)