from typing import Union

class Square:
    def __init__(self, side_length: Union[int, float]) -> None:
        self.side_length = side_length
    
    def area(self) -> Union[int, float]:
        return self.side_length ** 2

if __name__ == '__main__':
    sample_side1 = 7
    square1 = Square(sample_side1)
    print(f"Side: {sample_side1}, Area: {square1.area()}")

    sample_side2 = 9.5
    square2 = Square(sample_side2)
    print(f"Side: {sample_side2}, Area: {square2.area()}")