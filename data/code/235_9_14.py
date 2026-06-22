class LinePatternGenerator:
    @staticmethod
    def generate_line(length):
        return "*" * length

if __name__ == '__main__':
    generator = LinePatternGenerator()
    print(generator.generate_line(10))
    print(generator.generate_line(20))