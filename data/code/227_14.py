class StarPatternGenerator:
    def generate_hollow_square(self, n):
        if not isinstance(n, int) or n <= 0:
            return
        for i in range(n):
            line = ""
            for j in range(n):
                if i == 0 or i == n - 1 or j == 0 or j == n - 1:
                    line += "*"
                else:
                    line += " "
            print(line)
if __name__ == '__main__':
    generator = StarPatternGenerator()
    n_size = 5
    generator.generate_hollow_square(n_size)