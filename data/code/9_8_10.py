import numpy as np

def convert_volumes(measurements, source_unit, target_unit):
    base_cubic_meters = {
        "m3": 1.0,
        "cm3": 1e-6,
        "mm3": 1e-9,
        "l": 1e-3,
        "ml": 1e-6,
        "ft3": 0.028316846592,
        "in3": 1.6387064e-5,
        "gal_us": 0.003785411784,
        "qt_us": 0.000946352946,
        "pt_us": 0.000473176473,
    }
    
    source_factor = base_cubic_meters[source_unit]
    target_factor = base_cubic_meters[target_unit]
    
    volume_in_m3 = np.array(measurements, dtype=np.float64) * source_factor
    result = volume_in_m3 / target_factor
    return result

if __name__ == '__main__':
    sample_measurements = np.array([1.0, 100.0, 1000.0, 50.0, 0.5])
    results_liters = convert_volumes(sample_measurements, "m3", "l")
    results_gallons = convert_volumes(sample_measurements, "m3", "gal_us")
    results_cm3 = convert_volumes(sample_measurements, "ft3", "cm3")
    
    print("Results converting m3 to l:", results_liters)
    print("Results converting m3 to gal_us:", results_gallons)
    print("Results converting ft3 to cm3:", results_cm3)