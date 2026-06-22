class PatternGenerator:
    ROWS = 10
    COLS = 10

    @staticmethod
    def generate_pattern():
        pattern = []
        for i in range(PatternGenerator.ROWS):
            row = []
            for j in range(PatternGenerator.COLS):
                if (i + j) % 2 == 0:
                    row.append('*')
                else:
                    row.append('.')
            pattern.append(''.join(row))
        return '\n'.join(pattern)

if __name__ == '__main__':
    generator = PatternGenerator()
    print(generator.generate_pattern())