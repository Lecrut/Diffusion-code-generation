from typing import Union

class Square:
    def __init__(self, side_length: Union[int, float]) -> None:
        self.side_length = side_length
    
    def area(self) -> Union[int, float]:
        return self.side_length ** 2

if __name__ == '__main__':
    sample_side1 = 7
    square1 = Square(sample_side1)
    calculated_area1 = square1.area()
    print(f"Side: {sample_side1}, Area: {calculated_area1}")
    
    sample_side2 = 9.5
    square2 = Square(sample_side2)
    calculated_area2 = square2.area()
    print(f"Side: {sample_side2}, Area: {calculated_area2}")