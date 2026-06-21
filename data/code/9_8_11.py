import numpy as np

def convert_volumes(volumes_in_cubic_meters):
    liters = volumes_in_cubic_meters * 1000.0
    gallons = liters / 3.785411784
    return {
        'liters': liters,
        'gallons': gallons
    }

if __name__ == '__main__':
    sample_values = np.array([1.0, 2.5, 0.5, 10.0])
    results = convert_volumes(sample_values)
    print(results['liters'])
    print(results['gallons'])