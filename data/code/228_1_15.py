class TriangleGenerator:
    def generate_triangle(self, size):
        triangle = []
        for i in range(size):
            row = [1] * (i + 1)
            for j in range(1, i):
                row[j] = triangle[i-1][j-1] + triangle[i-1][j]
            triangle.append(row)
        return triangle

    def print_triangle(self, triangle):
        for row in triangle:
            print(' '.join(str(num).center(4) for num in row))

if __name__ == '__main__':
    generator = TriangleGenerator()
    triangle = generator.generate_triangle(5)
    generator.print_triangle(triangle)