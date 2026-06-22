class StarPatternGenerator:
    @staticmethod
    def generate_star_pattern(height):
        pattern = []
        for i in range(height):
            row = [' ' * (height - 1 - i) + '*' * (2 * i + 1) + ' ' * (height - 1 - i)]
            pattern.append(''.join(row))
        return pattern

if __name__ == '__main__':
    generator = StarPatternGenerator()
    sample_pattern = generator.generate_star_pattern(4)
    for line in sample_pattern:
        print(line)