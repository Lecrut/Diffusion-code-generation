def evaluate_boolean_expression(a, b, c, d):
    result1 = a and b
    result2 = not c
    result3 = a or d
    result4 = result1 and result2
    result5 = not_and(result3, result4)
    result6 = and_not(result5, result1)
    result7 = a == b
    result8 = c > d
    result9 = result7 or result8
    return result9
def not_and(x, y):
    return not (x and y)
def and_not(x, y):
    return (not x) and y
if __name__ == '__main__':
    a = True
    b = False
    c = True
    d = False
    print("--- Input Values ---")
    print(f"a: {a}")
    print(f"b: {b}")
    print(f"c: {c}")
    print(f"d: {d}\n")
    print("--- Intermediate Calculations ---")
    result1 = a and b
    print(f"result1 (a and b): {result1}")
    result2 = not c
    print(f"result2 (not c): {result2}")
    result3 = a or d
    print(f"result3 (a or d): {result3}")
    result4 = result1 and result2
    print(f"result4 (result1 and result2): {result4}")
    result5 = not_and(result3, result4)
    print(f"result5 (not_and(result3, result4)): {result5}")
    result6 = and_not(result5, result1)
    print(f"result6 (and_not(result5, result1)): {result6}")
    result7 = a == b
    print(f"result7 (a == b): {result7}")
    result8 = c > d
    print(f"result8 (c > d): {result8}")
    result9 = result7 or result8
    print(f"result9 (result7 or result8): {result9}")
    print("\n--- Final Result ---")
    print(f"Final result: {result9}")