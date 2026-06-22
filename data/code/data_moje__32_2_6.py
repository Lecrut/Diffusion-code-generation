from typing import Union

class Geometry:
    DEFAULT_WIDTH = 5.5
    DEFAULT_HEIGHT = 7.5

    @staticmethod
    def calculate_rectangle_area(width: Union[int, float], height: Union[int, float]) -> float:
        return float(width * height)

if __name__ == '__main__':
    sample_area = Geometry.calculate_rectangle_area(Geometry.DEFAULT_WIDTH, Geometry.DEFAULT_HEIGHT)
    print(sample_area)