if __name__ == '__main__':
    xor_gate = lambda a, b: a ^ b
    and_gate = lambda a, b: a & b
    or_gate = lambda a, b: a | b

    result_xor = xor_gate(1, 0)
    result_and = and_gate(1, 0)
    result_or = or_gate(1, 0)

    print(f"XOR: {result_xor}, AND: {result_and}, OR: {result_or}")