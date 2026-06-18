import math
from fractions import Fraction
from typing import Dict, Any

def simplify_ratio_weights(ratios_dict: Dict[Any, float]) -> Dict[str, int]:
    """
    Takes a dictionary where keys are ratio names and values are floating-point weight ratios.
    Returns a new dictionary with the same keys but simplified integer weights using Fraction arithmetic.
    
    Each value is converted to an irreducible fraction represented as integers (numerator, denominator).
    The resulting dictionaries map name -> tuple(int_num, int_den), where:
        - numerator * original_value ≈ original_weight
        - After simplification: num/den = simplified_fraction_of(original_value)

    :param ratios_dict: Dictionary with ratio names as keys and float weights as values.
    :return: New dictionary mapping name to tuple (simplified_numerator, simplified_denominator).
    """

if __name__ == '__main__':
    pass
