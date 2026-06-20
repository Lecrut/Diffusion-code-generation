bool_map = {True: False, False: True}

def are_booleans_equal(a, b):
    return bool_map[a] == bool_map[b]

if __name__ == '__main__':
    print(are_booleans_equal(True, True))
    print(are_booleans_equal(False, False))
    print(are_booleans_equal(True, False))