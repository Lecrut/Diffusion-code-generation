def combine_ratios(ratio1, ratio2, operation):
    if operation == "average":
        return (ratio1 + ratio2) / 2
    elif operation == "combined_product":
        return ratio1 * ratio2
    else:
        raise ValueError("Invalid operation specified")
if __name__ == '__main__':
    ratio1_val = 1
    ratio2_val = 2
    operation_type = "combined_product"
    result = combine_ratios(ratio1_val, ratio2_val, operation_type)
    print(f"Original Ratio 1:2")
    print(f"Operation: {operation_type}")
    print(f"Result: {result}")
    ratio_a = 1
    ratio_b = 2
    target_ratio = 3
    if operation_type == "average":
        new_avg = combine_ratios(ratio_a, ratio_b, "average")
        print(f"\nAverage of {ratio_a}:{ratio_b}: {new_avg}")
    else:
        external_constraint = 5
        new_ratio_1 = ratio_a * external_constraint
        new_ratio_2 = ratio_b * external_constraint
        print(f"\nApplying external constraint ({external_constraint}) to the original 1:2:")
        print(f"New Ratio: {new_ratio_1}:{new_ratio_2}")