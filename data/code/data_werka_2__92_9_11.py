TRUE_VAL = 1
FALSE_VAL = 0
BOOL_MAP = {TRUE_VAL: FALSE_VAL, FALSE_VAL: TRUE_VAL}

def find_opposite_truth(flag: bool) -> bool:
    if flag:
        return False
    return True

if __name__ == '__main__':
    val_true = find_opposite_truth(True)
    val_false = find_opposite_truth(False)
    print(val_true)
    print(val_false)