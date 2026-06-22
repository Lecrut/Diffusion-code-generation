from typing import Union

def compute_parallelogram_area(
    base: Union[int, float],
    height: Union[int, float]
) -> Union[int, float]:
    return base * height

if __name__ == '__main__':
    base_value = 10
    height_value = 5
    result = compute_parallelogram_area(base_value, height_value)
    print(result)