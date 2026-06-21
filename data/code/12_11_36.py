def validate_ratios(ratios):
    if not ratios:
        raise ValueError("Ratios list cannot be empty")
    if any(r <= 0 for r in ratios):
        raise ValueError("All ratios must be positive numbers")

def convert_ratios_to_weights(ratios, total_weight):
    validate_ratios(ratios)
    ratio_sum = sum(ratios)
    weights = [(ratio / ratio_sum) * total_weight for ratio in ratios]
    return weights

if __name__ == '__main__':
    sample_ratios = [1, 2, 3]
    total_weight = 60
    absolute_weights = convert_ratios_to_weights(sample_ratios, total_weight)
    print(absolute_weights)