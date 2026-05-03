def convert_ratios_to_weights(ratios, total_weight):
    weights = {}
    if not ratios:
        return weights
    sum_ratios = sum(ratios.values())
    if sum_ratios == 0:
        raise ValueError("Sum of ratios cannot be zero.")
    for item, ratio in ratios.items():
        weight = (ratio / sum_ratios) * total_weight
        weights[item] = weight
    return weights
if __name__ == '__main__':
    relative_ratios = {
        "ItemA": 1.0,
        "ItemB": 2.0,
        "ItemC": 3.0
    }
    total_weight = 100.0
    try:
        absolute_weights = convert_ratios_to_weights(relative_ratios, total_weight)
        print(absolute_weights)
    except ValueError as e:
        print(f"Error: {e}")