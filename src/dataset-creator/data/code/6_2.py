def compare_integers(a: int, b: int) -> bool:
    return a > b
def compare_floats(a: float, b: float) -> bool:
    if not (a == a and b == b):
        raise ValueError("NaN values detected")
    return a > b
def compare_strings(a: str, b: str) -> bool:
    return a > b
def is_greater(value_a, value_b):
    type_a = type(value_a).__name__
    type_b = type(value_b).__name__
    if type_a == 'int' and type_b == 'int':
        return compare_integers(value_a, value_b)
    elif type_a == 'float' and type_b == 'float':
        return compare_floats(value_a, value_b)
    elif type_a == 'str' and type_b == 'str':
        return compare_strings(value_a, value_b)
    else:
        raise TypeError(f"Unsupported types for comparison: {type_a} vs {type_b}")
if __name__ == '__main__':
    test_cases = [
        (10, 5),
        (3.14, 2.71),
        ("zebra", "apple"),
        (-1, -5),
        ("banana", "cherry")
    ]
    for a, b in test_cases:
        result = is_greater(a, b)
        print(f"{a} > {b}: {result}")