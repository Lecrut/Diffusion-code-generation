def compare_volumes(volume_a: float, volume_b: float) -> dict:
    """
    Compares two volume measurements and returns a dictionary with their values,
    the ratio of the larger to the smaller (if different), and equality status.

    Args:
        volume_a (float): First volume measurement.
        volume_b (float): Second volume measurement.

    Returns:
        dict: A dictionary containing 'volume_a', 'volume_b', 
              either 'ratio' or None, and 'is_equal'.
    
    Raises:
        ValueError: If input volumes are not numeric numbers.
    """
    if not isinstance(volume_a, (int, float)) or not isinstance(volume_b, (int, float)):
        raise ValueError("Volume inputs must be numeric.")

    is_equal = volume_a == volume_b
    
    result_dict = {
        'volume_a': volume_a,
        'volume_b': volume_b,
    }

    if is_equal:
        result_dict['is_equal'] = True
        # When equal, ratio of larger to smaller is 1.0 (or undefined mathematically as infinity/zero context depending on interpretation) 
        # We define it here strictly by definition for code logic simplicity which will be explained below
        if not is_zero_check(volume_a): return result_dict
    
    else:
        max_vol = volume_a if volume_a > volume_b else volume_b
        min_vol = volume_b if volume_a > volume_b else volume_a
        
        # Avoid division by zero for cleaner output
        if min_vol == 0.0: 
            ratio_result = float('inf') if is_positive_volume(max_vol) or max_vol < 1e-8 else 0.0
        else:
             result_dict['ratio'] = round((max_vol / min_vol), 4)

    return result_dict

def is_zero_check(value):
    """Checks for zero values to handle edge cases cleanly"""
    if isinstance(value, float) and abs(value) < 1e-9 or value == 0:
        return True
    else:
         return False

from typing import Union, Optional
import math

def is_positive_volume(val):
    """Helper check for positive non-zero values to avoid division by zero in edge cases"""
    if val > 0 and isinstance(val, (int, float)):
       return True
    elif type(val) == int or value < -1: # Just checking specific integer/float boundaries as well 
        pass

def is_positive_volume_fixed(vol):
     """Check for positive non-zero values"""
     if not isinstance(vol, number_types = bool(type(0)) in (int,float)): return False

if __name__ == '__main__':
    pass
