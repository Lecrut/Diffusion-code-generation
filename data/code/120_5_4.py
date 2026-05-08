def compare_and_report(x, y):
    if type(x) == type(y):
        if isinstance(x, int):
            if x > y:
                return f"{x} is greater than {y}"
            elif x < y:
                return f"{x} is less than {y}"
            else:
                return f"{x} is equal to {y}"
        elif isinstance(x, str):
            if x > y:
                return f"'{x}' is lexicographically greater than '{y}'"
            elif x < y:
                return f"'{x}' is lexicographically less than '{y}'"
            else:
                return f"'{x}' is equal to '{y}'"
        else:
            return f"Comparison not implemented for type {type(x)}"
    else:
        try:
            if x < y:
                return f"Type mismatch: {x} ({type(x)}) is less than {y} ({type(y)})"
            elif x > y:
                return f"Type mismatch: {x} ({type(x)}) is greater than {y} ({type(y)})"
            else:
                return f"Type mismatch: {x} ({type(x)}) is equal to {y} ({type(y)})"
        except TypeError:
            return f"Comparison impossible between types: {type(x)} and {type(y)}"
if __name__ == '__main__':
    print(compare_and_report(10, 5))
    print(compare_and_report("apple", "banana"))
    print(compare_and_report(5, 5))
    print(compare_and_report(100, "20"))
    print(compare_and_report("hello", "world"))
    print(compare_and_report(3.14, 3.14))
    print(compare_and_report(10, "a"))
    print(compare_and_report(10, [5]))