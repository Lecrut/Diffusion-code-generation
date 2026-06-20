def compare_and_report(x, y):
    if type(x) != type(y):
        raise TypeError(f"Type mismatch: Cannot directly compare {type(x)} and {type(y)}")
    
    if isinstance(x, (int, str)):
        if x < y:
            return f"Comparison: {x} < {y}"
        elif x > y:
            return f"Comparison: {x} > {y}"
        else:
            return f"Comparison: {x} == {y}"
    else:
        raise TypeError(f"Unsupported type for comparison between {type(x)} and {type(y)}")

if __name__ == '__main__':
    print("--- Integer Comparison ---")
    try:
        print(compare_and_report(10, 5))
        print(compare_and_report(20, 20))
        print(compare_and_report(3, 1))
    except TypeError as e:
        print(e)
    
    print("\n--- String Comparison ---")
    try:
        print(compare_and_report("apple", "banana"))
        print(compare_and_report("cherry", "cherry"))
        print(compare_and_report("date", "fig"))
    except TypeError as e:
        print(e)