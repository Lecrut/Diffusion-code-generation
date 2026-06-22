class PatternGenerator:
    @staticmethod
    def generate_hollow_square_line_pattern(size):
        if size < 2:
            return ""
        
        pattern = "*"
        for _ in range(1, size - 1):
            pattern += " "
        pattern += "*\n"
        
        middle_row = "*" * (size - 2) + "\n"
        
        for _ in range(size - 2):
            pattern += middle_row
        
        pattern += "*" * (size - 2) + "*"
        return pattern

if __name__ == '__main__':
    generator = PatternGenerator()
    print(generator.generate_hollow_square_line_pattern(5))