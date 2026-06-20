def logic_gates(a, b, c):
    return (a and b and c), (a or b or c), not a

if __name__ == '__main__':
    print(logic_gates(True, True, True))
    print(logic_gates(True, True, False))
    print(logic_gates(True, False, True))
    print(logic_gates(True, False, False))
    print(logic_gates(False, True, True))
    print(logic_gates(False, True, False))
    print(logic_gates(False, False, True))
    print(logic_gates(False, False, False))