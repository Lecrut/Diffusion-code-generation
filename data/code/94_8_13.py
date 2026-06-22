def check_truth_in_sequence(items):
    if not items:
        return False
    truth_map = {True: 'true', False: 'false'}
    status = {v: truth_map.get(v, 'unknown') for v in items}
    return any(k for k in status if k is True)

if __name__ == '__main__':
    test_data = [False, False, True, False]
    result = check_truth_in_sequence(test_data)
    print(result)