def compare_values(x, y):
    type_map = {
        int: lambda a, b: f"Comparison: {a} == {b}" if a == b else f"Comparison: {a} {'<' if a < b else '>'} {b}",
        str: lambda a, b: f"Comparison: '{a}' == '{b}'" if a == b else f"Comparison: '{a}' {'<' if a < b else '>'} '{b}'"
    }
    
    if type(x) in type_map and type(x) == type(y):
        return type_map[type(x)](x, y)
    else:
        return f"Type mismatch: Cannot directly compare {type(x)} and {type(y)}"

if __name__ == '__main__':
    print("--- Integer Comparison ---")
    print(compare_values(10, 5))
    print(compare_values(20, 20))
    print(compare_values(3, 1))

    print("--- String Comparison ---")
    print(compare_values("apple", "banana"))
    print(compare_values("cherry", "cherry"))
    print(compare_values("date", "apple"))