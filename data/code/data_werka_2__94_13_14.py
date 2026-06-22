def check_truthy_condition(sequence, predicate):
    truthy_lookup = {
        'found': True,
        'not_found': False,
    }
    result = truthy_lookup['not_found']
    iterator = iter(sequence)
    while True:
        try:
            item = next(iterator)
        except StopIteration:
            break
        if predicate(item):
            result = truthy_lookup['found']
            break
    return result

if __name__ == '__main__':
    sample_data = [0, None, False, 42, '']
    sample_predicate = lambda x: x is not None and x is not False and x != 0 and x != ''
    output = check_truthy_condition(sample_data, sample_predicate)
    print(output)