from typing import Union

class Square:
    def __init__(self, side_length: Union[int, float]) -> None:
        self.side_length = side_length
    
    def area(self) -> Union[int, float]:
        return self.side_length ** 2

if __name__ == '__main__':
    square_instance = Square(7)
    print(f"Side Length: {square_instance.side_length}, Area: {square_instance.area()}")
    
    square_instance = Square(3.5)
    print(f"Side Length: {square_instance.side_length}, Area: {square_instance.area()}")