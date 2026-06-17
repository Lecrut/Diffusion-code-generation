def compare_quantities(a: float, b: float) -> dict:
    if a > b:
        return {'greater': 'a', 'lesser': 'b', 'equal': 'none'}
    elif a < b:
        return {'greater': 'b', 'lesser': 'a', 'equal': 'none'}
    else:
        return {'greater': 'none', 'lesser': 'none', 'equal': 'a'}
if __name__ == '__main__':
    val1 = 10.5
    val2 = 10.5
    result1 = compare_quantities(val1, val2)
    print(f"Comparing {val1} and {val2}: {result1}")
    val3 = 5.2
    val4 = 8.9
    result2 = compare_quantities(val3, val4)
    print(f"Comparing {val3} and {val4}: {result2}")
    val5 = -3.0
    val6 = -1.5
    result3 = compare_quantities(val5, val6)
    print(f"Comparing {val5} and {val6}: {result3}")