# Simple weight difference calculation module
def calculate_weight_difference(var1: float, var2: float) -> float:
    """Returns the absolute difference between two numeric variables."""
    return abs(var1 - var2)

if __name__ == '__main__':
    sample_var_a = 50.0
    sample_var_b = 37.89
    result = calculate_weight_difference(sample_var_a, sample_var_b)
    print(result)