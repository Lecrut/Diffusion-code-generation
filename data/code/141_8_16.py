def compute_logic_gates(a, b, c):
    return (a and b and c), (a or b or c), not a

if __name__ == '__main__':
    results = [(compute_logic_gates(a, b, c) for c in [False, True]) for a in [False, True] for b in [False, True]]
    print(results)