def compare_and_report(x, y):
    if type(x) == type(y):
        if isinstance(x, int):
            if x < y:
                return f"Comparison: {x} < {y}"
            elif x > y:
                return f"Comparison: {x} > {y}"
            else:
                return f"Comparison: {x} == {y}"
        elif isinstance(x, str):
            if x < y:
                return f"Comparison: '{x}' < '{y}'"
            elif x > y:
                return f"Comparison: '{x}' > '{y}'"
            else:
                return f"Comparison: '{x}' == '{y}'"
        else:
            return f"Comparison Error: Unsupported type comparison between {type(x)} and {type(y)}"
    else:
        try:
            if x < y:
                return f"Comparison (Type Mismatch): {x} < {y} (Direct comparison)"
            elif x > y:
                return f"Comparison (Type Mismatch): {x} > {y} (Direct comparison)"
            else:
                return f"Comparison (Type Mismatch): {x} == {y} (Direct comparison)"
        except TypeError:
            return f"Comparison Error: Cannot directly compare {type(x)} and {type(y)}"
if __name__ == '__main__':
    print(compare_and_report(10, 5))
    print(compare_and_report("apple", "banana"))
    print(compare_and_report(5, 10))
    print(compare_and_report("hello", "world"))
    print(compare_and_report(10, "string"))
    print(compare_and_report(3.14, 2.71))
    print(compare_and_report(None, 1))