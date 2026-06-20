def logic_gates(a, b, c):
    return (a and b and c), (a or b or c), not a

if __name__ == '__main__':
    results = [logic_gates(i, j, k) for i in [False, True] for j in [False, True] for k in [False, True]]
    print(results)