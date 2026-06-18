import numpy as np

def convert_volume_to_cubic_meters(volumes_liters: np.ndarray) -> np.ndarray:
    """Converts an array of volumes from liters to cubic meters using vectorized NumPy operations."""
    return volumes_liters * 0.001

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input, args, or files)
    sample_volumes = np.array([250, 5000, 73948, 0])

    converted_results = convert_volume_to_cubic_meters(sample_volumes)

    print(f"Input volumes in liters: {sample_volumes}")
    print("Converted values to cubic meters:")
    for vol_liters, vol_m3 in zip(sample_volumes, converted_results):
        if len(vol_m3.shape) > 1:
            # Handle scalar array case by wrapping with list comprehension implicitly done via loop logic above since input is 0-dim per item effectively or just a flat view
            print(f"{vol_liters} L -> {float(vol_m3)} m³")
        else:
            print(f"{int(vol_liters)} L -> {float(vol_m3):.6f} m³")