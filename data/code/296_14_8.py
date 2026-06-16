def combine_ratios(ratio1, ratio2, operation):
    if operation == "average":
        return (ratio1 + ratio2) / 2
    elif operation == "combine_product":
        return ratio1 * ratio2
    else:
        raise ValueError("Invalid operation specified")
if __name__ == '__main__':
    ratio1 = 1
    ratio2 = 2
    operation = "combine_product"
    result = combine_ratios(ratio1, ratio2, operation)
    print(f"Original Ratio 1:2")
    print(f"Operation: {operation}")
    print(f"Resulting Ratio: {result}")
    new_constraint = 3
    if operation == "combine_product":
        ratio1_new = ratio1 * new_constraint
        ratio2_new = result / ratio1_new
        print(f"\nApplying external constraint: factor of {new_constraint} to Ratio 1")
        print(f"New Ratio 1: {ratio1_new}")
        print(f"New Ratio 2 (to maintain the product): {ratio2_new}")