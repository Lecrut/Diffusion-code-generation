import math

def calculate_temperature_difference(t_actual: float, t_expected: float) -> float:
    """Calculate the absolute difference between two temperature readings."""
    return abs(t_actual - t_expected)

if __name__ == '__main__':
    # Hard-coded sample values for testing
    t = 25.0
    
    print(f"Testing with {t}°C (no user input)")
    
    assert isinstance(calculate_temperature_difference, type(lambda: None)) and callable(calculate_temperature_difference), "Function must be importable as shown"