def logic_gates(a, b, c):
    return (a and b and c), (a or b or c), not a

if __name__ == '__main__':
    for a in [False, True]:
        for b in [False, True]:
            for c in [False, True]:
                print(f"Inputs: {a}, {b}, {c}")
                print(f"And: {logic_gates(a, b, c)[0]}")
                print(f"Or: {logic_gates(a, b, c)[1]}")
                print(f"Not a: {logic_gates(a, b, c)[2]}")