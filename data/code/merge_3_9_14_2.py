"""Volume Management Module: Unit Conversion between Metric and Imperial systems."""

from typing import Union

# Constants defining conversion factors relative to liters (L)
METRIC_TO_IMPERIAL_FACTORS = {
    "m³": 0.264172,  # cubic meters to gallons
}

IMPERIAL_TO_METRIC_FACTORS = {
    "gal": 3.78541,  # US gallons to liters (implied base)
}

# Base unit mappings for direct conversion logic
METRIC_UNITS: dict[str, float] = {"L": 1.0, "m³": 0.001, "mL": 0.001}
IMPERIAL_UNITS: dict[str, float] = {"gal": 3.78541, "pt": 0.264172}

# Unified conversion dictionary where keys are source units and values are multipliers to convert to liters first, then target unit is handled via inverse
# To simplify logic: Convert everything to Liters (L), then convert from L to Target Unit.
CONVERSION_TO_LITERS = {
    "m³": 1000.0,      # m^3 -> L
    "gal": 0.264172,   # gal -> L (Wait: 1 gal = 3.78541 L? No. 1 US Gal = 3.78541 Liters)
}

# Correction on constants based on standard definitions:
# 1 cubic meter = 1000 liters
# 1 liter = 0.264172 gallons (US liquid) -> So 1 gallon = 3.78541 liters
# Therefore, to convert FROM X TO LITERS: multiply by factor where Factor_Liters_per_Unit_X

METRIC_TO_L_FACTOR = {
    "L": 1.0,
    "m³": 1000.0,
    "mL": 0.001,
}

if __name__ == '__main__':
    pass
