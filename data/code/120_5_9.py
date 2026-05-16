def compare_and_report(x, y):
    if type(x) == type(y):
        if isinstance(x, int) or isinstance(x, str):
            if x < y:
                print(f"Comparison: {x} < {y}")
            elif x > y:
                print(f"Comparison: {x} > {y}")
            else:
                print(f"Comparison: {x} == {y}")
        else:
            print(f"Error: Comparison not supported for type {type(x)} and {type(y)}")
    else:
        print(f"Type mismatch: Cannot directly compare {type(x)} and {type(y)}")
if __name__ == '__main__':
    print("--- Integer Comparison ---")
    compare_and_report(10, 5)
    compare_and_report(20, 20)
    compare_and_report(3, 1)
    print("\n--- String Comparison ---")
    compare_and_report("apple", "banana")
    compare_and_report("hello", "world")
    compare_and_report("test", "test")
    print("\n--- Mixed Type Comparison ---")
    compare_and_report(10, "hello")
    compare_and_report("hello", 10)
    compare_and_report(10, [1, 2])