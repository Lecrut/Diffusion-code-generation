class TriangleGenerator:
    def generate_triangle(self, n):
        return [[1] * (i + 1) for i in range(n)]

if __name__ == '__main__':
    generator = TriangleGenerator()
    triangle = generator.generate_triangle(5)
    print(triangle)