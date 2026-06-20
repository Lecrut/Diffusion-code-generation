def truth_table_implication(a, b):
    return not a or b

def truth_table_equivalence(a, b):
    return a == b
if __name__ == '__main__':
    print(truth_table_implication(True, True))
    print(truth_table_implication(True, False))
    print(truth_table_implication(False, True))
    print(truth_table_implication(False, False))
    print(truth_table_equivalence(True, True))
    print(truth_table_equivalence(True, False))
    print(truth_table_equivalence(False, True))
    print(truth_table_equivalence(False, False))