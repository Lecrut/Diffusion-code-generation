def is_equivalent(p, q):
    from itertools import product

    def truth_values(formula):
        if formula == 'P':
            return True
        elif formula == 'Q':
            return False
        elif formula == '!P':
            return not truth_values('P')
        elif formula == '!Q':
            return not truth_values('Q')
        elif formula == 'P & Q':
            return truth_values('P') and truth_values('Q')
        elif formula == 'P | Q':
            return truth_values('P') or truth_values('Q')
    for assignment in product([True, False], repeat=2):
        if truth_values(p) != truth_values(q):
            return False
    return True
if __name__ == '__main__':
    print(is_equivalent('P & Q', 'Q & P'))
    print(is_equivalent('P | !P', 'True'))