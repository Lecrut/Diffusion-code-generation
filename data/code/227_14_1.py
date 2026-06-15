class StarPatternGenerator:
    def generate_hollow_square(self, n):
        for i in range(n):
            row = ""
            for j in range(n):
                if i == 0 or i == n - 1 or j == 0 or j == n - 1:
                    row += "*"
                else:
                    row += " "
            print(row)
if __name__ == '__main__':
    generator = StarPatternGenerator()
    size = 5
    generator.generate_hollow_square(size)