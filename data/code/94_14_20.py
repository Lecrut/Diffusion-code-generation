def has_any_true(values):
    truth_lookup = {True: True, False: False}
    result = False
    iterator = iter(values)
    while True:
        try:
            item = next(iterator)
            if truth_lookup.get(item, False):
                result = True
                break
        except StopIteration:
            break
    return result

if __name__ == '__main__':
    data = [False, False, True, False]
    outcome = has_any_true(data)
    print(outcome)