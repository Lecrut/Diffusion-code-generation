def compare_and_report(x, y):
    if type(x) != type(y):
        return f"Type mismatch: Cannot directly compare {type(x).__name__} and {type(y).__name__}"
    if isinstance(x, (int, str)):
        if x < y:
            return f"Comparison: {x} < {y}"
        elif x > y:
            return f"Comparison: {x} > {y}"
        else:
            return f"Comparison: {x} == {y}"
    else:
        return "Error: Unsupported type for comparison"

if __name__ == '__main__':
    print("--- Integer Comparison ---")
    print(compare_and_report(10, 5))
    print(compare_and_report(20, 20))
    print(compare_and_report(3, 1))

    print("--- String Comparison ---")
    print(compare_and_report("apple", "banana"))
    print(compare_and_report("banana", "apple"))
    print(compare_and_report("cherry", "cherry"))

    print("--- Unsupported Type Comparison ---")
    print(compare_and_report([1, 2], (3, 4)))