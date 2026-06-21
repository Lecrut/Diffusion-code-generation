def both_false_generator(a, b):
    mapping = {
        (False, False): True,
        (False, True): False,
        (True, False): False,
        (True, True): False,
    }
    yield mapping.get((a, b), False)

if __name__ == '__main__':
    samples = [
        (False, False),
        (True, False),
        (False, True),
        (True, True),
    ]
    for val_a, val_b in samples:
        result = list(both_false_generator(val_a, val_b))
        print(result[0])