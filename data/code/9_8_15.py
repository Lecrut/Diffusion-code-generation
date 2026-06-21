import numpy as np

def convert_volumes(volumes, from_unit, to_unit):
    conversion_factors = {
        ("ml", "ml"): 1.0,
        ("ml", "l"): 1e-3,
        ("ml", "gal"): 2.64172e-4,
        ("ml", "floz"): 3.3814e-2,
        ("ml", "tsp"): 0.202884,
        ("ml", "tbsp"): 0.067628,
        ("ml", "cup"): 0.00422675,
        ("l", "ml"): 1e3,
        ("l", "l"): 1.0,
        ("l", "gal"): 0.264172,
        ("l", "floz"): 33.814,
        ("l", "tsp"): 202.884,
        ("l", "tbsp"): 67.628,
        ("l", "cup"): 4.22675,
        ("gal", "ml"): 3785.41,
        ("gal", "l"): 3.78541,
        ("gal", "gal"): 1.0,
        ("gal", "floz"): 128.0,
        ("gal", "tsp"): 768.0,
        ("gal", "tbsp"): 256.0,
        ("gal", "cup"): 16.0,
        ("floz", "ml"): 29.5735,
        ("floz", "l"): 2.95735e-2,
        ("floz", "gal"): 7.8125e-3,
        ("floz", "floz"): 1.0,
        ("floz", "tsp"): 6.0,
        ("floz", "tbsp"): 2.0,
        ("floz", "cup"): 0.125,
        ("tsp", "ml"): 4.92892,
        ("tsp", "l"): 4.92892e-3,
        ("tsp", "gal"): 1.30208e-3,
        ("tsp", "floz"): 0.166667,
        ("tsp", "tsp"): 1.0,
        ("tsp", "tbsp"): 0.333333,
        ("tsp", "cup"): 0.0208333,
        ("tbsp", "ml"): 14.7868,
        ("tbsp", "l"): 1.47868e-2,
        ("tbsp", "gal"): 3.90625e-3,
        ("tbsp", "floz"): 0.5,
        ("tbsp", "tsp"): 3.0,
        ("tbsp", "tbsp"): 1.0,
        ("tbsp", "cup"): 0.0625,
        ("cup", "ml"): 236.588,
        ("cup", "l"): 0.236588,
        ("cup", "gal"): 0.0625,
        ("cup", "floz"): 8.0,
        ("cup", "tsp"): 48.0,
        ("cup", "tbsp"): 16.0,
        ("cup", "cup"): 1.0,
    }
    if from_unit not in conversion_factors or to_unit not in conversion_factors:
        raise ValueError(f"Unsupported units: {from_unit} to {to_unit}")
    pair = (from_unit, to_unit)
    if pair not in conversion_factors:
        raise ValueError(f"No direct conversion factor from {from_unit} to {to_unit}")
    factor = conversion_factors[pair]
    return np.asarray(volumes, dtype=float) * factor

if __name__ == '__main__':
    sample_volumes = np.array([100.0, 250.0, 500.0, 1000.0, 2500.0])
    converted = convert_volumes(sample_volumes, "ml", "l")
    print(converted)