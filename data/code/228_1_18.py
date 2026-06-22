class TriangleGenerator:
    def generate_triangle(self, height):
        triangle = []
        for i in range(height):
            row = [1] * (i + 1)
            for j in range(1, i):
                row[j] = triangle[i-1][j-1] + triangle[i-1][j]
            triangle.append(row)
        return triangle

if __name__ == '__main__':
    generator = TriangleGenerator()
    triangle = generator.generate_triangle(5)
    print(triangle)