def convert_ratios_to_weights(ratios, total_weight):
    weights = {}
    if not ratios:
        return weights
    sum_ratios = sum(ratios)
    if sum_ratios == 0:
        raise ValueError("Sum of ratios cannot be zero.")
    for ratio in ratios:
        weight = (ratio / sum_ratios) * total_weight
        weights[ratio] = weight
    return weights
if __name__ == '__main__':
    sample_ratios = [1, 2, 3]
    sample_total_weight = 100
    try:
        absolute_weights = convert_ratios_to_weights(sample_ratios, sample_total_weight)
        print(absolute_weights)
    except ValueError as e:
        print(f"Error: {e}")