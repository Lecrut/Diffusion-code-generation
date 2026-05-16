import operator
def evaluate_conditions(cond1, cond2, cond3, cond4):
    result = cond1 and cond2 or cond3 and cond4
    return result
if __name__ == '__main__':
    a = True
    b = False
    c = True
    d = False
    result = evaluate_conditions(a, b, c, d)
    print(f"a = {a}")
    print(f"b = {b}")
    print(f"c = {c}")
    print(f"d = {d}")
    print(f"Result of (a and b) or (c and d): {result}")