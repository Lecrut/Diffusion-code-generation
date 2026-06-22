import numpy as np

def vectorized_volume_conversion(measurements, source_unit="m3", target_unit="L"):
    conversion_factors = {
        "m3_to_L": 1000.0,
        "L_to_m3": 0.001,
        "gal_to_L": 3.78541,
        "L_to_gal": 0.264172,
        "ft3_to_L": 28.3168,
        "L_to_ft3": 0.0353147,
        "cup_to_L": 0.24,
        "L_to_cup": 4.16667,
    }
    key = f"{source_unit}_to_{target_unit}"
    if key not in conversion_factors:
        raise ValueError(f"Unsupported conversion from {source_unit} to {target_unit}")
    measurements = np.asarray(measurements, dtype=float)
    return measurements * conversion_factors[key]

if __name__ == "__main__":
    sample_measurements = np.array([1.0, 2.5, 5.0, 10.0, 0.5])
    converted = vectorized_volume_conversion(sample_measurements, "m3", "L")
    print(converted)
    converted_gal = vectorized_volume_conversion(sample_measurements, "L", "gal")
    print(converted_gal)