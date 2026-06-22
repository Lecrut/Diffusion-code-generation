class LinePatternGenerator:
    @staticmethod
    def generate_line(n):
        return "*" * n

if __name__ == '__main__':
    generator = LinePatternGenerator()
    print(generator.generate_line(10))
    print(generator.generate_line(5))
    print(generator.generate_line(1))