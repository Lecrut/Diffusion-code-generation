def check_both_false(val_a, val_b):
    mapping = {
        (True, True): False,
        (True, False): False,
        (False, True): False,
        (False, False): True
    }
    return mapping[(val_a, val_b)]

if __name__ == '__main__':
    result = check_both_false(False, False)
    print(result)