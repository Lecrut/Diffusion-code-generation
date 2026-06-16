def compare_quantities(a: float, b: float) -> dict:
    if a > b:
        return {'greater': 'a', 'lesser': 'b', 'equal': 'none'}
    elif a < b:
        return {'greater': 'b', 'lesser': 'a', 'equal': 'none'}
    else:
        return {'greater': 'none', 'lesser': 'none', 'equal': 'a'}
if __name__ == '__main__':
    num1 = 10.5
    num2 = 5.2
    result1 = compare_quantities(num1, num2)
    print(f"Comparing {num1} and {num2}: {result1}")
    num3 = 7.0
    num4 = 7.0
    result2 = compare_quantities(num3, num4)
    print(f"Comparing {num3} and {num4}: {result2}")
    num5 = 3.14
    num6 = 3.14159
    result3 = compare_quantities(num5, num6)
    print(f"Comparing {num5} and {num6}: {result3}")