def combine_ratios(ratio1, ratio2, method='average'):
    if method == 'average':
        return (ratio1 + ratio2) / 2
    elif method == 'product':
        return ratio1 * ratio2
    else:
        raise ValueError("Invalid combination method")
if __name__ == '__main__':
    ratio1_val = 1
    ratio2_val = 2
    combination_method = 'average'
    result = combine_ratios(ratio1_val, ratio2_val, combination_method)
    print(f"Original Ratio 1:2")
    print(f"Combination Method: {combination_method}")
    print(f"Resulting Ratio: {result}:1")
    external_constraint = 5
    new_ratio1 = result * external_constraint
    new_ratio2 = (ratio1_val + ratio2_val) * external_constraint
    print("\n--- Applying External Constraint ---")
    print(f"External Constraint: {external_constraint}")
    print(f"New Ratio 1 based on constraint: {new_ratio1}:{new_ratio2}")