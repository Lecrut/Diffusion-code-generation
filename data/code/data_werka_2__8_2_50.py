class PolygonAreaCalculator:
    def __init__(self, vertices):
        self.vertices = vertices

    def calculate_area(self):
        n = len(self.vertices)
        if n < 3:
            raise ValueError("A polygon must have at least 3 vertices")
        
        total_area = 0.0
        for i in range(n):
            x1, y1 = self.vertices[i]
            x2, y2 = self.vertices[(i + 1) % n]
            total_area += (x1 * y2 - x2 * y1)
        
        return abs(total_area) / 2.0

if __name__ == '__main__':
    sample_vertices = [(5, 3), (8, 6), (7, 9)]
    calculator = PolygonAreaCalculator(sample_vertices)
    print(calculator.calculate_area())