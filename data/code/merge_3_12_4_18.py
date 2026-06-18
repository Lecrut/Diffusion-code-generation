import math
from fractions import Fraction

def simplify_ratios(weight_ratios):
    """
    Takes a list of weight ratios (as lists/tuples or floats) 
    and returns a new list containing simplified forms as tuples of integers.
    
    A ratio is represented by two numbers [a, b]. The simplification process:
    1. Converts the pair to a Fraction if they are not already exact integers.
    2. Finds the greatest common divisor (GCD) of numerator and denominator.
    3. Divides both parts by this GCD to get the simplest form.
    
    Args:
        weight_ratios (list): List of ratios, where each ratio is a sequence 
                              representing [part1, part2]. Can be floats or ints.
                              
    Returns:
        list: A new list containing tuples of simplified integer parts for each input ratio.
              If the denominator becomes 0 after simplification, it returns (numerator, None).
    
    Example:
        >>> simplify_ratios([[1, 2], [3.5, 4.5]])
        [(1, 2), (7, 9)]
    """
    simplified_list = []

    for ratio in weight_ratios:
        # Ensure input is a sequence of two elements
        if not isinstance(ratio, (list, tuple)):
            raise TypeError(f"Each element must be a list or tuple with at least two numbers. Got {type(ratio)}")

if __name__ == '__main__':
    pass
