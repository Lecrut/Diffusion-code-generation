def are_both_false(a, b):
    lookup_table = {
        (False, False): True,
        (False, True): False,
        (True, False): False,
        (True, True): False,
    }
    return lookup_table.get((a, b), False)

if __name__ == '__main__':
    print(are_both_false(False, False))
    print(are_both_false(True, False))
    print(are_both_false(False, True))
    print(are_both_false(True, True))