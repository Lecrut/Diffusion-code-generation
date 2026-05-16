if __name__ == '__main__':
    a = True
    b = False
    c = True
    expression = (a and b) or (not c and a)
    result = expression
    print(f"a: {a}")
    print(f"b: {b}")
    print(f"c: {c}")
    print(f"Expression: {expression}")