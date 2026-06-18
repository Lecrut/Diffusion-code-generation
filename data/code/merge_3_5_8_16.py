"""
Module to convert length measurements between feet and meters 
and compute absolute and percentage differences.

Since no input prompt is required, this module uses hard-coded sample values 
in its main block to demonstrate functionality.
"""

def feet_to_meters(feet: float) -> float:
    """Convert a value in feet to meters."""
    return feet * 0.3048

def compare_lengths(value_a: float, unit_a: str, value_b: float, unit_b: str) -> dict[str, float]:
    """
    Compare two length values given their respective units.

    Args:
        value_a (float): The first measurement value.
        unit_a (str): The unit of the first measurement ('ft' or 'm').
        value_b (float): The second measurement value.
        unit_b (str): The unit of the second measurement ('ft' or 'm').

    Returns:
        dict: A dictionary containing absolute difference and percentage difference in meters.
    """
    # Ensure units are strings for processing if they come as other types, though inputs will be floats here based on task constraint regarding input(). However, unit args should remain string logic safe.
    
    def normalize_to_meters(val, u):
        return val * (0.3048 if u == 'ft' else 1)

    meters_a = normalize_to_meters(value_a, unit_a.lower())
    meters_b = normalize_to_meters(value_b, unit_b.lower())

    absolute_diff = abs(meters_a - meters_b)

    # Calculate percentage difference relative to the average of the two values 
    # to avoid division by zero if both are zero (though lengths usually aren't).
    avg_val = (meters_a + meters_b) / 2.0
    
    if avg_val == 0:
        pct_diff = 0.0
    else:
        diff_from_avg = abs(meters_a - meters_b) / 2 # Equivalent to relative difference between them * 100 compared to scale, 
                                                       # but standard formula is |a-b|/((a+b)/2)*100 which simplifies to |diff|*2/(sum).
        pct_diff = (absolute_diff / avg_val) * 100

if __name__ == '__main__':
    pass
