import numpy as np

def vectorized_volume_conversion(volume_values, source_unit, target_unit):
    conversion_factors = {
        ('ml', 'l'): 0.001,
        ('l', 'ml'): 1000.0,
        ('gal', 'l'): 3.78541,
        ('l', 'gal'): 0.264172,
        ('cu_ft', 'l'): 28.3168,
        ('l', 'cu_ft'): 0.0353147,
        ('cu_in', 'l'): 0.0163871,
        ('l', 'cu_in'): 61.0237,
        ('tbsp', 'ml'): 14.7868,
        ('ml', 'tbsp'): 0.067628,
        ('tsp', 'ml'): 4.92892,
        ('ml', 'tsp'): 0.202884,
        ('cup', 'ml'): 236.588,
        ('ml', 'cup'): 0.00422675,
        ('pt', 'l'): 0.473176,
        ('l', 'pt'): 2.11338,
        ('qt', 'l'): 0.946353,
        ('l', 'qt'): 1.05669,
    }
    if (source_unit, target_unit) in conversion_factors:
        return volume_values * conversion_factors[(source_unit, target_unit)]
    elif source_unit == target_unit:
        return volume_values.copy()
    else:
        raise ValueError(f"Unsupported conversion from {source_unit} to {target_unit}")

if __name__ == '__main__':
    sample_volumes = np.array([100, 250, 500, 1000, 2500])
    converted = vectorized_volume_conversion(sample_volumes, 'ml', 'l')
    print(converted)