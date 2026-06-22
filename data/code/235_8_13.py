class ArrowheadPattern:
    def __init__(self, width):
        self.width = width

    def generate_pattern(self):
        pattern = ""
        for i in range(1, self.width + 1):
            pattern += "*" * i + "\n"
        return pattern.rstrip()

if __name__ == '__main__':
    arrowhead = ArrowheadPattern(5)
    print(arrowhead.generate_pattern())