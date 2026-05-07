def main():
    a = True
    b = False
    c = True
    print("--- Test Case 1: a or b ---")
    result1 = a or b
    print(f"a: {a}, b: {b}")
    print(f"a or b is: {result1}")
    print("\n--- Test Case 2: a or c ---")
    result2 = a or c
    print(f"a: {a}, c: {c}")
    print(f"a or c is: {result2}")
    print("\n--- Test Case 3: b or c ---")
    result3 = b or c
    print(f"b: {b}, c: {c}")
    print(f"b or c is: {result3}")
    print("\n--- Test Case 4: False or False ---")
    x = False
    y = False
    result4 = x or y
    print(f"x: {x}, y: {y}")
    print(f"x or y is: {result4}")
    print("\n--- Test Case 5: True or False ---")
    p = True
    q = False
    result5 = p or q
    print(f"p: {p}, q: {q}")
    print(f"p or q is: {result5}")
if __name__ == '__main__':
    main()