class TriangleArt:
    def __init__(self, base_length=10):
        self.base_length = base_length

    def generate_art(self):
        return '\n'.join('*' * i for i in range(1, self.base_length + 1))

if __name__ == '__main__':
    triangle = TriangleArt()
    print(triangle.generate_art())