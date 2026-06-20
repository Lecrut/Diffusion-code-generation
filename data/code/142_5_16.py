def compare_boolean_values(value1: bool, value2: bool) -> bool:
    return value1 == value2

if __name__ == '__main__':
    sample_value1 = True
    sample_value2 = False
    result = compare_boolean_values(sample_value1, sample_value2)
    print(f"Value 1: {sample_value1}, Value 2: {sample_value2}, Result: {result}")