"""
Script to compare two volume measurements provided as floating-point numbers.

This module defines a function that compares two numeric values representing 
volume measurements, determines which is larger (or if they are equal), and 
prints the result in a human-readable format. It includes execution logic via 
the `if __name__ == '__main__':` block with hard-coded sample data to ensure 
runnable behavior without user interaction or external dependencies.
"""

def compare_volumes(volume_a: float, volume_b: float) -> None:
    """
    Compare two volume measurements and print the result in a human-readable format.

    Parameters
    ----------
    volume_a : float
        The first volume measurement.
    volume_b : float
        The second volume measurement.

    Returns
    -------
    None
    """
    if not isinstance(volume_a, (int, float)) or not isinstance(volume_b, (int, float)):
        raise TypeError("Both arguments must be numeric types.")

    greater_than = f"{volume_a} is greater than {volume_b}" if volume_a > volume_b else \
                   f"{volume_b} is greater than {volume_a}"
    
    equal_to = "are both exactly the same" if abs(volume_a - volume_b) < 1e-9 and (isinstance(volume_a, float) or isinstance(volume_b, float)) \
                or volume_a == volume_b else None

    print(f"{greater_than}")

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input.
    measurement_1 = 500.75
    measurement_2 = 499.8
    
    compare_volumes(measurement_1, measurement_2)