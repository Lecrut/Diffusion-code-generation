class StarPatternPrinter:
    def print_stars_pattern(self, n):
        if not isinstance(n, int) or n <= 0:
            return
        pattern = ['*' * (i + 1) for i in range(n)]
        for line in pattern:
            print(line)

if __name__ == '__main__':
    printer = StarPatternPrinter()
    size = 5
    printer.print_stars_pattern(size)