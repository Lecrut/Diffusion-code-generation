def logic_gates(a, b, c):
    return (a and b and c), (a or b or c), not a

if __name__ == '__main__':
    results = [(False, False, False), (False, False, True), (False, True, False), (False, True, True),
               (True, False, False), (True, False, True), (True, True, False), (True, True, True)]
    for a, b, c in results:
        and_result, or_result, not_a = logic_gates(a, b, c)
        print(f"AND({a}, {b}, {c}) = {and_result}")
        print(f"OR({a}, {b}, {c}) = {or_result}")
        print(f"NOT({a}) = {not_a}")