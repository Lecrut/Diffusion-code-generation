import math

def scale_volumes(volumes: list[float], factor: float) -> list[float]:
    """
    Scale a given list of volume values by a specified floating-point factor.

    Args:
        volumes (list[float]): The initial list of volume data.
        factor (float): The scaling multiplier for each volume value.

    Returns:
        list[float]: A new list containing the scaled volume values.
    
    Note: Uses standard float arithmetic which maintains sufficient precision 
    for most scientific and engineering applications involving typical volume ranges.
    """
    if not isinstance(volumes, (list, tuple)):
        raise TypeError("Input 'volumes' must be a list or tuple of numbers.")
    if factor == 0:
        return [0.0] * len(volumes)

    scaled = []
    for vol in volumes:
        try:
            new_vol = float(vol) * factor
            # Ensure the result is treated as a standard Python float (IEEE 754 double precision)
            if isinstance(new_vol, int):
                new_vol = float(new_vol)
            scaled.append(new_vol)
        except TypeError:
            raise ValueError(f"Unsupported data type in volumes list: {type(vol)}")

    return scaled

if __name__ == '__main__':
    # Hard-coded sample values representing initial volume measurements (e.g., liters or cubic meters)
    initial_volumes = [10.5, 23.75, 45.0, 89.1, 12.3]
    
    # Define a scaling factor for demonstration purposes (e.g., converting to milliliters: x1000)
    scale_factor = 1000.0

    scaled_result = scale_volumes(initial_volumes, scale_factor)

    print("Original volumes:", initial_volumes)
    print(f"Scaling by factor {scale_factor}:")
    print("Scaled volumes:", scaled_result)
    
    # Verification: check that all elements are floats and precision is maintained
    assert isinstance(scaled_result[0], float), "Result must contain floating-point numbers."
    for i, val in enumerate(scaled_result):
        expected = initial_volumes[i] * scale_factor
        if abs(val - expected) > 1e-6:
            raise AssertionError(f"Precision error detected at index {i}: got {val}, expected approx {expected}")

    print("Verification passed: Floating-point precision maintained correctly.")