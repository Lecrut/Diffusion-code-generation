def check_nested_conditions():
    a = True
    b = False
    c = True
    return (a and b) or (c and not b)

if __name__ == '__main__':
    result = check_nested_conditions()
    print(f"Result of nested boolean expression: {result}")