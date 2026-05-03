def convert_ratios_to_weights(ratios, total_weight):
    weights = {}
    if not ratios:
        return weights
    sum_ratios = sum(ratios)
    if sum_ratios == 0:
        raise ValueError("Sum of ratios cannot be zero.")
    for ratio in ratios:
        weights[ratio] = (ratio / sum_ratios) * total_weight
    return weights
if __name__ == '__main__':
    relative_ratios = [1, 2, 3]
    total_weight_value = 100
    try:
        absolute_weights = convert_ratios_to_weights(relative_ratios, total_weight_value)
        print(absolute_weights)
    except ValueError as e:
        print(f"Error: {e}")