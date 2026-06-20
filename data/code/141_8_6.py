def logic_gates(a, b, c):
    return a & b & c, a | b | c, not (a or b or c)

if __name__ == '__main__':
    results = [logic_gates(a, b, c) for a in [False, True] for b in [False, True] for c in [False, True]]
    print(results)