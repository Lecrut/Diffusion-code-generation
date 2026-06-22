def both_false_generator(a, b):
    lookup = {
        (False, False): True,
        (False, True): False,
        (True, False): False,
        (True, True): False,
    }
    yield lookup.get((a, b), False)

if __name__ == '__main__':
    print(list(both_false_generator(False, False)))
    print(list(both_false_generator(True, False)))
    print(list(both_false_generator(False, True)))
    print(list(both_false_generator(True, True)))