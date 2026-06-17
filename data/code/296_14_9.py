def combine_ratios(ratio1, ratio2, method):
    if method == "average":
        return (ratio1 + ratio2) / 2
    elif method == "product":
        return ratio1 * ratio2
    else:
        raise ValueError("Invalid combination method")
if __name__ == '__main__':
    ratio1_val = 1
    ratio2_val = 2
    combination_method = "average"
    result = combine_ratios(ratio1_val, ratio2_val, combination_method)
    print(f"Original Ratio 1:2")
    print(f"Combining using {combination_method}: {result}")
    external_constraint = 5
    new_ratio1 = result * external_constraint
    new_ratio2 = result / external_constraint
    print(f"\nExternal Constraint: {external_constraint}")
    print(f"New Ratio derived from combination: {new_ratio1}:{new_ratio2}")