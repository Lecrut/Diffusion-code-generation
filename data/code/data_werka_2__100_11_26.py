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
    sample_list = [True, True, True]
    result = check_all_boolean_values(sample_list, "all_true")
    print(result)