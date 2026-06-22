import numpy as np

def convert_volumes(volumes_cm3):
    liters = volumes_cm3 / 1000.0
    gallons = liters / 3.785411784
    cubic_inches = volumes_cm3 / 16.387064
    return {
        'liters': liters,
        'gallons': gallons,
        'cubic_inches': cubic_inches
    }

if __name__ == '__main__':
    sample_volumes = np.array([1000, 500, 3785.411784])
    result = convert_volumes(sample_volumes)
    print(result)