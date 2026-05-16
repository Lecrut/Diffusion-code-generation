def compare_and_report(x, y):
    if type(x) == type(y):
        if isinstance(x, int):
            if x > y:
                return f"Comparison: {x} > {y}"
            elif x < y:
                return f"Comparison: {x} < {y}"
            else:
                return f"Comparison: {x} == {y}"
        elif isinstance(x, str):
            if x > y:
                return f"Comparison: '{x}' > '{y}'"
            elif x < y:
                return f"Comparison: '{x}' < '{y}'"
            else:
                return f"Comparison: '{x}' == '{y}'"
        else:
            return f"Comparison Error: Unsupported type {type(x)} vs {type(y)}"
    else:
        try:
            if x < y:
                return f"Comparison (Mixed Types): {x} < {y}"
            elif x > y:
                return f"Comparison (Mixed Types): {x} > {y}"
            else:
                return f"Comparison (Mixed Types): {x} == {y}"
        except TypeError:
            return f"Comparison Error: Cannot compare {type(x)} and {type(y)} directly."
if __name__ == '__main__':
    print(compare_and_report(10, 5))
    print(compare_and_report(20, 20))
    print(compare_and_report("apple", "banana"))
    print(compare_and_report("cat", "dog"))
    print(compare_and_report(5, "hello"))
    print(compare_and_report(3.14, 3.14))
    print(compare_and_report(10, "10"))