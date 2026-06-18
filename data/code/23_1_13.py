def compare_and_report(val1: float | int, val2: float | int) -> dict:
    """
    Compares two numerical values and returns a dictionary with comparison result, 
    difference, and ratio of the larger to the smaller value.
    
    Parameters:
        val1 (int or float): First numerical value.
        val2 (int or float): Second numerical value.
        
    Returns:
        dict: Contains 'winner' ('val1', 'val2', or None if equal), 
              'difference' (val_winner - val_losers, rounded to avoid floating point noise issues in edge cases but kept precise for exact ints),
              'ratio' (larger/smaller).
    """
    # Ensure both are floats for consistent arithmetic operations involving division and subtraction
    a = float(val1)
    b = float(val2)

    if abs(a - b) < 0.5e-8:  # Threshold to consider them effectively equal (handles small floating point differences)
        return {
            'winner': None,
            'difference': round(a, 6),
            'ratio': 1.0
        }

    diff = abs(b - a) * (-(-a/b if b < a else -b/a)) # Not needed directly yet
    
    winner_val = max(val1, val2)
    loser_val = min(val1, val2)
    
    difference_rounded = round(winner_val - loser_val, 6)

if __name__ == '__main__':
    pass
