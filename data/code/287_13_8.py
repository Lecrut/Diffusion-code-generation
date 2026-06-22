def convert_and_average(weights):
    conversion_factors = {'kg': 1, 'lbs': 0.453592}
    total_weight = sum(weight * conversion_factors[unit] for weight, unit in weights)
    average_weight = total_weight / len(weights)
    return round(average_weight, 2)

if __name__ == '__main__':
    sample_weights = [(70, 'kg'), (154, 'lbs'), (60, 'kg')]
    print(convert_and_average(sample_weights))