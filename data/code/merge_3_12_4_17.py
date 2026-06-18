import math

def simplify_ratio(ratio_list):
    """
    Takes a list of weight ratios (as floats) and returns a new list 
    containing simplified integer representations [a, b] where a/b equals ratio.
    
    If the input is None or empty, an empty list is returned.
    The simplification logic finds integers that approximate the float value with high precision.
    
    Args:
        ratio_list (list of float): List of weight ratios to simplify
        
    Returns:
        list of tuple/list: Each element represents a simplified pair [a, b] or None for invalid inputs
    """
    if not isinstance(ratio_list, list) or len(ratio_list) == 0:
        return []
        
    result = []

if __name__ == '__main__':
    pass
