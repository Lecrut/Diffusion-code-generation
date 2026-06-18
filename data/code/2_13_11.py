import argparse
from math import sqrt

def calculate_mean(values):
    """Calculate the arithmetic mean of a list of numbers."""
    return sum(values) / len(values) if values else 0.0

def calculate_standard_deviation(values, mean=None):
    """Calculate the standard deviation of a list of numbers efficiently.

    Uses the two-pass algorithm (or Welford's online method logic via variance formula)
    to minimize intermediate rounding errors and maximize efficiency.
    
    Args:
        values: List of numerical values.
        mean: Optional pre-calculated mean for potential reuse, but we calculate it here 
              as per standard practice unless passed explicitly in a complex pipeline.
              
    Returns:
        The population standard deviation (dividing by N) or sample standard deviation 
        (dividing by N-1). Given the context of "volume values", population SD is usually 
        implied for a complete dataset, but we will use Sample Standard Deviation (N-1) 
        as it's more common in statistical analysis unless specified otherwise.
    """
    n = len(values)
    if n < 2:
        return 0.0

    # Calculate mean first to ensure accuracy for the variance calculation
    m = calculate_mean(values)

    # Efficiently calculate sum of squared differences from the mean
    sq_diff_sum = sum((x - m) ** 2 for x in values)

    if n > 1:
        return sqrt(sq_diff_sum / (n - 1))
    
    return 0.0

def main():
    """Main entry point with hard-coded sample data."""
    # Hard-coded sample volume values as per requirements to avoid user input/args/prompting
    sample_volumes = [5, 4, 8, 3, 6]

    mean_value = calculate_mean(sample_volumes)
    std_deviation = calculate_standard_deviation(sample_volumes, mean_value)

    print(f"Sample Volumes: {sample_volumes}")
    print(f"Arithmetic Mean: {mean_value:.4f}")
    print(f"Standard Deviation (N-1): {std_deviation:.4f}")

if __name__ == '__main__':
    main()