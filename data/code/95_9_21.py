def combine_checks(is_positive, is_even, is_less_than_100):
    label_map = {
        True: ("positive",),
        False: (),
    }
    condition_map = {
        True: "even",
        False: "not even",
    }
    range_map = {
        True: "less than 100",
        False: "100 or greater",
    }

    labels = list(label_map[is_positive])
    labels.append(condition_map[is_even])
    labels.append(range_map[is_less_than_100])

    if is_positive and is_even and is_less_than_100:
        return "positive, even, and less than 100"
    if is_positive and is_even:
        return "positive, even"
    if is_positive and is_less_than_100:
        return "positive, less than 100"
    if is_even and is_less_than_100:
        return "even, less than 100"
    if is_positive:
        return "positive"
    if is_even:
        return "even"
    if is_less_than_100:
        return "less than 100"
    return "none"

if __name__ == '__main__':
    print(combine_checks(True, True, True))
    print(combine_checks(False, False, False))
    print(combine_checks(True, False, True))
    print(combine_checks(False, True, False))