def boolean_gates(a, b, c):
    return (a and b and c), (a or b or c), not a

if __name__ == '__main__':
    for a in [False, True]:
        for b in [False, True]:
            for c in [False, True]:
                print(f"a={a}, b={b}, c={c}")
                and_result, or_result, not_a = boolean_gates(a, b, c)
                print(f"AND: {and_result}, OR: {or_result}, NOT a: {not_a}")