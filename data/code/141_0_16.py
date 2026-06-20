def logical_gate(A, B):
    operations = {'AND': A & B, 'OR': A | B, 'NOT': not A if B else A}
    return operations
if __name__ == '__main__':
    result_and = logical_gate(True, True)
    result_or = logical_gate(False, True)
    result_not = logical_gate(True, False)
    print(result_and)
    print(result_or)
    print(result_not)