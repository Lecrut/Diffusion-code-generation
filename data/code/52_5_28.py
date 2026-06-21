from typing import Union

class Rectangle:

    def __init__(self, length: Union[int, float], width: Union[int, float]):
        if length < 0 or width < 0:
            raise ValueError('Length and width must be non-negative numbers.')
        self.length = length
        self.width = width

    def calculate_area(self) -> Union[int, float]:
        return self.length * self.width
if __name__ == '__main__':
    sample_length = 6.5
    sample_width = 2.0
    rectangle = Rectangle(sample_length, sample_width)
    area = rectangle.calculate_area()
    print(area)
    perimeter = 2 * (sample_length + sample_width)
    print(perimeter)