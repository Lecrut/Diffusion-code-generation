class RightAngledTriangle:
    def __init__(self, height):
        self.height = height
        self.triangle = [[1] * (i + 1) for i in range(height)]

if __name__ == '__main__':
    triangle = RightAngledTriangle(5)
    print(triangle.triangle)