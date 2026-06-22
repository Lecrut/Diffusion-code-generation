import numpy as np

CONVERSION_FACTORS = {
    "cubic_meters": 1.0,
    "liters": 1000.0,
    "gallons": 264.172,
    "cubic_inches": 61023.7
}

def convert_volumes(volumes_in_cubic_meters, target_unit="liters"):
    if target_unit not in CONVERSION_FACTORS:
        raise ValueError(f"Unsupported target unit: {target_unit}")
    
    factor = CONVERSION_FACTORS[target_unit]
    return np.array(volumes_in_cubic_meters, dtype=np.float64) * factor

if __name__ == '__main__':
    sample_volumes = [1.5, 2.0, 0.5, 10.0]
    result = convert_volumes(sample_volumes, "gallons")
    print(result)