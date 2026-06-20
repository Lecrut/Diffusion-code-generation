def logic_gates(a, b, c):
    return a and b and c, a or b or c, not (a or b or c)

if __name__ == '__main__':
    for a in [False, True]:
        for b in [False, True]:
            for c in [False, True]:
                print(f"a={a}, b={b}, c={c}")
                and_result, or_result, not_a = logic_gates(a, b, c)
                print(f"AND: {and_result}, OR: {or_result}, NOT a: {not_a}")