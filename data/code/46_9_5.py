class Triangle:
    def __init__(self, sides):
        self.sides = sides
        if any(side <= 0 for side in sides):
            raise ValueError("All sides must be positive numbers.")
    
    def perimeter(self):
        return sum(self.sides)
    
    def is_equilateral(self):
        return len(set(self.sides)) == 1

if __name__ == '__main__':
    triangle_sides = [7, 7, 7]
    my_triangle = Triangle(triangle_sides)
    print(my_triangle.perimeter())
    print(my_triangle.is_equilateral())