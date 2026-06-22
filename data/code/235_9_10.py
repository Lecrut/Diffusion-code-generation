class LinePatternGenerator:
    @staticmethod
    def generate_line(n):
        return "*" * n

if __name__ == '__main__':
    pattern = LinePatternGenerator.generate_line(10)
    print(pattern)