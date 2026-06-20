def compare_booleans(a, b):
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