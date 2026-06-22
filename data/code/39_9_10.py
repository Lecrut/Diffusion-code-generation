from typing import Union

Number = Union[int, float]

def calculate_prism_volume(base_area: Number, height: Number) -> Number:
    return base_area * height

if __name__ == '__main__':
    base: Number = 50
    height: Number = 10
    volume: Number = calculate_prism_volume(base, height)
    print(volume)