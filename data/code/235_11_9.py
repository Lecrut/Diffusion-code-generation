class DiamondRenderer:
    def __init__(self, size):
        self.size = size

    def render(self):
        for i in range(self.size):
            print(' ' * (self.size - i - 1) + '*' * (2 * i + 1))
        for i in range(self.size-2, -1, -1):
            print(' ' * (self.size - i - 1) + '*' * (2 * i + 1))

if __name__ == '__main__':
    renderer = DiamondRenderer(5)
    renderer.render()