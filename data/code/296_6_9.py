def validate_ratios(ratios):
    for ratio in ratios:
        if not isinstance(ratio, tuple) or len(ratio) != 2:
            raise ValueError("Each ratio must be a tuple of two numbers.")
        if ratio[1] == 0:
            raise ValueError("Denominator cannot be zero.")

def validate_multiplier(multiplier):
    if not isinstance(multiplier, (int, float)):
        raise ValueError("Multiplier must be a number.")

def harmonic_mean_of_ratios(ratios):
    validate_ratios(ratios)
    
    sum_reciprocals = 0
    for ratio in ratios:
        sum_reciprocals += ratio[1] / ratio[0]
    
    if sum_reciprocals == 0:
        raise ValueError("Sum of reciprocals cannot be zero.")
    
    return len(ratios) / sum_reciprocals

if __name__ == '__main__':
    sample_ratios = [(1, 2), (3, 4), (5, 6)]
    sample_multiplier = 1.5
    result = harmonic_mean_of_ratios(sample_ratios)
    print(result)