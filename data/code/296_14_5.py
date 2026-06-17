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
    print(f"Resulting value: {result}")
    external_constraint = 5
    if operation == "combine_product":
        new_ratio_part1 = result / external_constraint
        new_ratio_part2 = result * external_constraint
        print(f"New Ratio based on constraint ({external_constraint}): {new_ratio_part1}:{new_ratio_part2}")