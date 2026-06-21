def calculate_total_ratio(ratios):
    return sum(ratios)

def convert_ratios_to_weights(ratios, total_weight):
    ratio_sum = calculate_total_ratio(ratios)
    weights = [(ratio / ratio_sum) * total_weight for ratio in ratios]
    return weights

if __name__ == '__main__':
    sample_ratios = [2, 3, 5]
    total_weight = 100
    absolute_weights = convert_ratios_to_weights(sample_ratios, total_weight)
    print(absolute_weights)