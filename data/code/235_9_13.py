class LinePatternGenerator:
    @staticmethod
    def generate_line_pattern(length):
        if not isinstance(length, int) or length <= 0:
            raise ValueError("Length must be a positive integer")
        
        for i in range(length):
            print("*" * (i + 1))

if __name__ == '__main__':
    LinePatternGenerator.generate_line_pattern(5)