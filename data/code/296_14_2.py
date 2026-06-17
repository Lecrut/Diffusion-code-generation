def combine_ratios(ratio1, ratio2, method):
    if method == "average":
        return (ratio1 + ratio2) / 2
    elif method == "combined":
        return (2) / (1/ratio1 + 1/ratio2)
    else:
        raise ValueError("Invalid method specified")
if __name__ == '__main__':
    ratio1_input = 1
    ratio2_input = 2
    combination_method = "combined"
    result = combine_ratios(ratio1_input, ratio2_input, combination_method)
    print(f"Original Ratio 1:2")
    print(f"Combining ratios {ratio1_input}:{ratio2_input} using the '{combination_method}' method results in: {result}")