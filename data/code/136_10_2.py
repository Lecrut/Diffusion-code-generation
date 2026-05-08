def main():
    a = True
    b = False
    c = True
    print("--- Logical Operators Demonstration ---")
    print(f"a = {a}, b = {b}, c = {c}")
    and_result = a and b
    or_result = a or b
    not_a_result = not a
    xor_result = a ^ b
    print("\n--- AND Operator (a and b) ---")
    print(f"a and b: {and_result}")
    print("\n--- OR Operator (a or b) ---")
    print(f"a or b: {or_result}")
    print("\n--- NOT Operator (not a) ---")
    print(f"not a: {not_a_result}")
    print("\n--- XOR Operator (a XOR b) ---")
    print(f"a XOR b: {xor_result}")
if __name__ == '__main__':
    main()