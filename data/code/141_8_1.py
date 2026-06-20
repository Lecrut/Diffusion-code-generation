def boolean_gates(a, b, c):
    return (a and b and c), (a or b or c), not a

if __name__ == '__main__':
    results = [(a, b, c, *boolean_gates(a, b, c)) for a in [False, True] for b in [False, True] for c in [False, True]]
    for result in results:
        print(result)