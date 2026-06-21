def check_all_boolean_values(values, condition="all_true"):
    if not values:
        return False
    if condition == "all_true":
        return all(values)
    elif condition == "all_false":
        return all(not v for v in values)
    else:
        raise ValueError(f"Unsupported condition: {condition}")

if __name__ == '__main__':
    sample_values = [True, True, True]
    result_true = check_all_boolean_values(sample_values, "all_true")
    print(result_true)
    sample_values_false = [False, False, False]
    result_false = check_all_boolean_values(sample_values_false, "all_false")
    print(result_false)
    sample_values_mixed = [True, False, True]
    result_mixed = check_all_boolean_values(sample_values_mixed, "all_true")
    print(result_mixed)