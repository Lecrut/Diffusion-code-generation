class TriangleGenerator:
    MAX_HEIGHT = 5

    @staticmethod
    def generate_triangle(height):
        if height > TriangleGenerator.MAX_HEIGHT or height <= 0:
            raise ValueError("Height must be between 1 and 5")
        for i in range(1, height + 1):
            print("*" * i)

if __name__ == '__main__':
    triangle_height = 5
    try:
        TriangleGenerator.generate_triangle(triangle_height)
    except ValueError as e:
        print(e)