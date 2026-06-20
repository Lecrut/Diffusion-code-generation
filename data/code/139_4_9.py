AND_GATE = lambda a, b: a & b
OR_GATE = lambda a, b: a | b
NOT_GATE = lambda a: ~a + 1 if a else 0
if __name__ == '__main__':
    print(AND_GATE(1, 1))
    print(AND_GATE(1, 0))
    print(OR_GATE(1, 0))
    print(NOT_GATE(1))
    print(NOT_GATE(0))