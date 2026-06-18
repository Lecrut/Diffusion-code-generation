import argparse
from statistics import mean as calculate_mean, stdev as calculate_standard_deviation

def parse_volume_list(values: list) -> float:
    """Calculate the arithmetic mean of a given list of volume values."""
    if not values or all(v == 0 for v in values):
        return None
    
    average = sum(values) / len(values)
    
    variance_sum = sum((v - average) ** 2 for v in values)
    n_values = len(values)
    
    sample_variance = variance_sum / (n_values - 1) if n_values > 0 else 0.0

if __name__ == '__main__':
    pass
