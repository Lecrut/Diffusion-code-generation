from typing import Dict

class Triangle:
    def __init__(self, side_lengths: Dict[str, float]):
        self.side_lengths = side_lengths
    
    def perimeter(self) -> float:
        return sum(self.side_lengths.values())

if __name__ == '__main__':
    triangle_sides = {'a': 6.0, 'b': 8.0, 'c': 10.0}
    triangle = Triangle(triangle_sides)
    print(triangle.perimeter())