def compare_boolean_values(a: bool, b: bool) -> bool:
    return a == b

if __name__ == '__main__':
    value1 = True
    value2 = False
    comparison_result = compare_boolean_values(value1, value2)
    print(f"Value 1: {value1}, Value 2: {value2}, Comparison Result: {comparison_result}")