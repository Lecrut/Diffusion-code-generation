TRUE_VALS = {True, 1, 1.0, 'yes', 'true', 'on', 'enabled', [1], (1,), {1}, {1: 1}, b'1'}
FALSE_VALS = {False, 0, 0.0, '', 'no', 'false', 'off', 'disabled', [], (), {}, set(), b'', None}

def determine_both_false(val1, val2):
    truth_table = {
        True: True,
        False: False,
        None: False,
        0: False,
        1: True,
        '': False,
        '0': False,
        '1': True,
        []: False,
        {}: False,
        (): False,
    }
    val1_bool = truth_table.get(val1, bool(val1))
    val2_bool = truth_table.get(val2, bool(val2))
    return not val1_bool and not val2_bool

if __name__ == '__main__':
    r1 = determine_both_false(False, False)
    print(r1)
    r2 = determine_both_false(None, None)
    print(r2)
    r3 = determine_both_false([], {})
    print(r3)
    r4 = determine_both_false(0, 0.0)
    print(r4)
    r5 = determine_both_false('', '')
    print(r5)
    r6 = determine_both_false(1, 1)
    print(r6)
    r7 = determine_both_false(True, True)
    print(r7)
    r8 = determine_both_false([1], {1: 1})
    print(r8)
    r9 = determine_both_false(0, 1)
    print(r9)
    r10 = determine_both_false(False, True)
    print(r10)