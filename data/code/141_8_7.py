def logic_gates(a, b, c):
    return (a and b and c), (a or b or c), not a

if __name__ == '__main__':
    results = [(x, y, z) for x in [False, True] for y in [False, True] for z in [False, True]]
    for result in results:
        print(logic_gates(*result))