def combine_ratios(ratio1, ratio2, operation):
    if operation == "average":
        return (ratio1 + ratio2) / 2
    elif operation == "combined_product":
        return ratio1 * ratio2
    else:
        raise ValueError("Invalid operation specified")
if __name__ == '__main__':
    ratio1 = 1
    ratio2 = 2
    operation = "combined_product"
    result = combine_ratios(ratio1, ratio2, operation)
    print(f"Original Ratio 1:2")
    print(f"Operation: {operation}")
    print(f"Resulting Ratio: {result}")
    external_constraint = 5
    new_ratio1 = result / external_constraint
    new_ratio2 = result * external_constraint
    print("\n--- External Constraint Demonstration ---")
    print(f"External Constraint: {external_constraint}")
    print(f"New Ratio 1: {new_ratio1}: {new_ratio2}")