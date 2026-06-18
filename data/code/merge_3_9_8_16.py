import numpy as np

def convert_volume_to_cubic_meters(volume_liters: float) -> float:
    """Convert a volume in liters to cubic meters."""
    return volume_liters * 0.001

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or files
    sample_volumes = np.array([5, 234.7, 1000, -10, 0])

    # Perform vectorized conversion to cubic meters
    volumes_cubic_meters = convert_volume_to_cubic_meters(sample_volumes) * (np.ones_like(sample_volumes))

    print("Original Liters:", sample_volumes)
    print("Converted Cubic Meters:", np.round(volumes_cubic_meters, 6))