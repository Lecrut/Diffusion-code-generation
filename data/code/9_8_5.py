import numpy as np

def convert_volume(volume_liters: float) -> dict:
    """Convert a single volume in liters to cubic meters, gallons (US), quarts (US), pints (US), and milliliters."""
    m3 = volume_liters * 0.001
    gal_us = volume_liters * 264.172052
    qt_us = volume_liters * 8.79876913
    pt_us = volume_liters * 17.5975383
    ml = volume_liters * 1000

    return {
        'cubic_meters': m3,
        'gallons_us': gal_us,
        'quarts_us': qt_us,
        'pints_us': pt_us,
        'milliliters': ml
    }

def vectorized_convert(volumes: np.ndarray) -> dict:
    """Perform volume conversions for an entire array of measurements using NumPy vectorization."""
    return {
        'cubic_meters': volumes * 0.001,
        'gallons_us': volumes * 264.172052,
        'quarts_us': volumes * 8.79876913,
        'pints_us': volumes * 17.5975383,
        'milliliters': volumes * 1000
    }

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    sample_volumes = np.array([1.5, 2.0, 5.75])

    result_vectorized = vectorized_convert(sample_volumes)

    print("Vectorized Volume Conversion Results:")
    print("-" * 40)
    
    # Print results for each input value to demonstrate the array operation clearly
    for i in range(len(result_vectorized['cubic_meters'])):
        v_liters = sample_volumes[i]
        conversions = {
            'liters': f"{v_liters}",
            'm3': result_vectorized['cubic_meters'][i],
            'gal_us': round(result_vectorized['gallons_us'][i], 2),
            'qt_us': round(result_vectorized['quarts_us'][i], 2),
            'pt_us': round(result_vectorized['pints_us'][i], 2),
            'ml': result_vectorized['milliliters'][i]
        }

        print(f"Input: {conversions['liters']} L")
        for unit, value in conversions.items():
            if unit != 'liters':
                print(f"{unit}: {value}")