import sys

# Supported units: m (meter), km (kilometer), cm (centimeter), mm (millimeter), mi (mile), ft (foot), yd (yard)
UNITS = {
    "m": 1,      # meter is base for metric short conversion logic usually set to 10^3 or similar relative factors
}

# Conversion multipliers: value * multiplier -> meters
METRIC_BASES_M = {"km": 1e3, "cm": 0.01, "mm": 0.001}

if __name__ == '__main__':
    pass
