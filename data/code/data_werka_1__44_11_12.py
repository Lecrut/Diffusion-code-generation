class ShapeCalculator:
    def __init__(self):
        self.shapes = []

    def add_rectangle(self, length: float, width: float):
        if length <= 0 or width <= 0:
            raise ValueError("Length and width must be positive numbers.")
        self.shapes.append((length, width))

    def calculate_perimeter(self, shape_index: int) -> float:
        if not self.shapes:
            raise IndexError("No shapes added to the calculator.")
        length, width = self.shapes[shape_index]
        return 2 * (length + width)

if __name__ == '__main__':
    try:
        calc = ShapeCalculator()
        calc.add_rectangle(10.5, 5.0)
        calc.add_rectangle(7.2, 4.8)
        
        perimeter1 = calc.calculate_perimeter(0)
        print(perimeter1)
        
        perimeter2 = calc.calculate_perimeter(1)
        print(perimeter2)
    except (ValueError, IndexError) as e:
        print(e)