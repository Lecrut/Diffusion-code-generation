def logic_gates(a, b, c):
    return a & b & c, a | b | c, not (a or b or c)

if __name__ == '__main__':
    results = [(x, y, z) for x in [False, True] for y in [False, True] for z in [False, True]]
    for result in results:
        and_result, or_result, not_result = logic_gates(*result)
        print(f"Inputs: {result}, AND: {and_result}, OR: {or_result}, NOT: {not_result}")