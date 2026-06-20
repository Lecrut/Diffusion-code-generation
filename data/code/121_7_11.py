def compare_int_quantity(quantity1: int, quantity2: int) -> bool:
    if not isinstance(quantity1, int) or not isinstance(quantity2, int):
        raise ValueError("Both inputs must be integers.")
    return quantity1 > quantity2

if __name__ == '__main__':
    sample_value1 = 5
    sample_value2 = 3
    result = compare_int_quantity(sample_value1, sample_value2)
    print(f"Comparing {sample_value1} and {sample_value2}: {result}")