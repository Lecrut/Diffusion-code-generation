def find_maximum(*args):
    if not args:
        return None
    maximum = args[0]
    for arg in args[1:]:
        if arg > maximum:
            maximum = arg
    return maximum
if __name__ == '__main__':
    result1 = find_maximum(10, 5, 20, 8)
    print(f"Maximum of (10, 5, 20, 8): {result1}")
    result2 = find_maximum(-5, -1, -10)
    print(f"Maximum of (-5, -1, -10): {result2}")
    result3 = find_maximum(42)
    print(f"Maximum of (42): {result3}")
    result4 = find_maximum()
    print(f"Maximum of (): {result4}")
    result5 = find_maximum(3.14, 2.71, 1.618)
    print(f"Maximum of (3.14, 2.71, 1.618): {result5}")