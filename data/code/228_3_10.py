class RightAngledTriangle:
    def __init__(self, height):
        self.height = height

    def generate_triangle(self):
        return '\n'.join(' '.join(str(i) for i in range(1, j + 1)) for j in range(1, self.height + 1))

if __name__ == '__main__':
    triangle1 = RightAngledTriangle(3)
    print(triangle1.generate_triangle())
    
    triangle2 = RightAngledTriangle(5)
    print(triangle2.generate_triangle())