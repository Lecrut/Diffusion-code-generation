class StarPatternGenerator:
    @staticmethod
    def generate_pattern(height):
        pattern = []
        for i in range(height):
            row = ['*'] if i == 0 else [' '] * (height - i - 1) + ['*'] + [' '] * i
            pattern.append(''.join(row))
        return pattern

if __name__ == '__main__':
    generator = StarPatternGenerator()
    print(generator.generate_pattern(4))