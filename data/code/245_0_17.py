class ShapeAreaCalculator:

    def calculate_area(self, vertices):
        n = len(vertices)
        area = 0.5 * abs(sum((vertices[i][0] * vertices[(i + 1) % n][1] - vertices[i][1] * vertices[(i + 1) % n][0] for i in range(n))))
        return area
if __name__ == '__main__':
    calculator = ShapeAreaCalculator()
    triangle_vertices = [(0, 0), (4, 0), (2, 3)]
    triangle_area = calculator.calculate_area(triangle_vertices)
    print(f'Triangle Area: {triangle_area}')
    quad_vertices = [(0, 0), (5, 0), (5, 5), (0, 5)]
    quad_area = calculator.calculate_area(quad_vertices)
    print(f'Quadrilateral Area: {quad_area}')
    if triangle_area == quad_area:
        print('The areas of the two shapes are equal.')
    else:
        print('The areas of the two shapes are not equal.')