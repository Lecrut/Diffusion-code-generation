def main():
    a = True
    b = False
    c = True
    print("--- Testing 'or' operator ---")
    condition1 = a or b
    print(f"a is {a}, b is {b}")
    print(f"a or b is: {condition1}")
    condition2 = b or c
    print(f"b is {b}, c is {c}")
    print(f"b or c is: {condition2}")
    condition3 = a or c
    print(f"a is {a}, c is {c}")
    print(f"a or c is: {condition3}")
    condition4 = False or False
    print(f"False or False is: {condition4}")
    condition5 = True or False
    print(f"True or False is: {condition5}")
    condition6 = True or True
    print(f"True or True is: {condition6}")
if __name__ == '__main__':
    main()