class PatternGenerator:
    def generate_checkerboard(self, rows, cols):
        pattern = []
        for i in range(rows):
            row_str = ""
            for j in range(cols):
                if (i + j) % 2 == 0:
                    row_str += 'X'
                else:
                    row_str += ' '
            pattern.append(row_str)
        return pattern
if __name__ == '__main__':
    generator = PatternGenerator()
    rows = 5
    cols = 7
    checkerboard = generator.generate_checkerboard(rows, cols)
    for row in checkerboard:
        print(row)