class RightAngledTriangle:
    def __init__(self, height):
        self.height = height
        self.triangle = [[1] * (i + 1) for i in range(height)]

    def display(self):
        for row in self.triangle:
            print(row)

if __name__ == '__main__':
    triangle = RightAngledTriangle(5)
    triangle.display()