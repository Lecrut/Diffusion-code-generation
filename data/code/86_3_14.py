def compare_booleans(a, b):
    if not isinstance(a, bool) or not isinstance(b, bool):
        raise ValueError("Both inputs must be boolean values.")
    return [a == b]

if __name__ == '__main__':
    samples = [
        (True, False),
        (True, True),
        (False, True)
    ]
    for sample in samples:
        result = compare_booleans(*sample)
        print(result)