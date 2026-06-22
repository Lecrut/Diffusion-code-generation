from typing import Union

Number = Union[int, float]

def calculate_prism_volume(base_area: Number, height: Number) -> float:
    return float(base_area * height)

if __name__ == '__main__':
    sample_base_area: float = 25.5
    sample_height: float = 10
    volume: float = calculate_prism_volume(sample_base_area, sample_height)
    print(volume)