def main():
    a = True
    b = False
    c = True
    print("--- Test Case 1: a or b (True or False) ---")
    result1 = a or b
    print(f"a: {a}, b: {b}")
    print(f"Result of a or b: {result1}")
    print("\n--- Test Case 2: a or c (True or True) ---")
    result2 = a or c
    print(f"a: {a}, c: {c}")
    print(f"Result of a or c: {result2}")
    print("\n--- Test Case 3: b or c (False or True) ---")
    result3 = b or c
    print(f"b: {b}, c: {c}")
    print(f"Result of b or c: {result3}")
    print("\n--- Test Case 4: b or b (False or False) ---")
    result4 = b or b
    print(f"b: {b}")
    print(f"Result of b or b: {result4}")
    print("\n--- Test Case 5: False or True (False or True) ---")
    result5 = False or True
    print(f"False: {False}, True: {True}")
    print(f"Result of False or True: {result5}")
if __name__ == '__main__':
    main()