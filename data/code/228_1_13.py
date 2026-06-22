class TriangleGenerator:
    def generate_triangle(self, height):
        triangle = []
        for i in range(1, height + 1):
            row = [1] * i
            for j in range(1, i - 1):
                row[j] = triangle[i-2][j-1] + triangle[i-2][j]
            triangle.append(row)
        return triangle

if __name__ == '__main__':
    generator = TriangleGenerator()
    triangle = generator.generate_triangle(5)
    for row in triangle:
        print(row)