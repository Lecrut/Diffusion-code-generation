"""Volume Management Module.

This module provides functions to convert between metric (liters, milliliters, cubic meters)
and imperial (gallons) volume units. It adheres to Python best practices including type hinting
and uses only standard library features.
"""

# Conversion constants
METRIC_TO_IMPERIAL = {
    "L": 0.264172052,      # Liters to Gallons
    "mL": 0.000264172052, # Milliliters to Gallons
    "m³": 264.172052,     # Cubic meters to Gallons (approx)
}

IMPERIAL_TO_METRIC = {
    "gal": 3.785411784,      # Gallons to Liters
    "L": 1.0,                 # Liters to Liters (identity for reference if needed)
    "m³": 0.003785411784,   # Cubic meters to Liters
}

if __name__ == '__main__':
    pass
