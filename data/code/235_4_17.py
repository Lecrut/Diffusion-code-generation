class HollowRectangleGenerator:
    WIDTH = 6
    HEIGHT = 4

    @staticmethod
    def generate_pattern():
        pattern = []
        for i in range(HollowRectangleGenerator.HEIGHT):
            if i == 0 or i == HollowRectangleGenerator.HEIGHT - 1:
                pattern.append('*' * HollowRectangleGenerator.WIDTH)
            else:
                line = '*' + ' ' * (HollowRectangleGenerator.WIDTH - 2) + '*'
                pattern.append(line)
        return pattern

if __name__ == '__main__':
    generator = HollowRectangleGenerator()
    pattern = generator.generate_pattern()
    for line in pattern:
        print(line)