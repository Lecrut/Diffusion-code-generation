from typing import List

class Triangle:
    def __init__(self, sides: List[float]):
        self.sides = sides

    def is_valid(self) -> bool:
        a, b, c = self.sides
        return (a > 0 and b > 0 and c > 0) and (a + b > c and a + c > b and b + c > a)

    def get_perimeter(self) -> float:
        if not self.is_valid():
            raise ValueError("Invalid triangle sides")
        return sum(self.sides)

if __name__ == '__main__':
    sample_sides = [3.0, 4.0, 5.0]
    t = Triangle(sample_sides)
    print(t.get_perimeter())
    print(f"Is the triangle valid? {t.is_valid()}")