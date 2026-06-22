from typing import Union

VolumeValue = Union[int, float]

def calculate_prism_volume(base_area: VolumeValue, height: VolumeValue) -> VolumeValue:
    if not isinstance(base_area, (int, float)):
        raise TypeError("Base area must be a number")
    if not isinstance(height, (int, float)):
        raise TypeError("Height must be a number")
    if base_area <= 0 or height <= 0:
        raise ValueError("Base area and height must be positive values")
    return base_area * height

if __name__ == '__main__':
    sample_base_area: float = 15.5
    sample_height: int = 8
    result: VolumeValue = calculate_prism_volume(sample_base_area, sample_height)
    print(result)