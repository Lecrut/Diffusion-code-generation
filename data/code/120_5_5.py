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
                return f"Comparison (Mixed Types): {x} < {y}"
            elif x > y:
                return f"Comparison (Mixed Types): {x} > {y}"
            else:
                return f"Comparison (Mixed Types): {x} == {y}"
        except TypeError:
            return f"Comparison Error: Cannot directly compare {type(x)} and {type(y)}"
if __name__ == '__main__':
    print(compare_and_report(10, 5))
    print(compare_and_report("apple", "banana"))
    print(compare_and_report(5, 10))
    print(compare_and_report("hello", "world"))
    print(compare_and_report(10, "a"))
    print(compare_and_report(3.14, 3.14))
    print(compare_and_report(10, "hello"))
    print(compare_and_report(None, 5))