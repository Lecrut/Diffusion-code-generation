class HeartPattern:
    def __init__(self):
        self.pattern = [
            "  *****",
            " **   *",
            "*     *",
            "*     *",
            " *   * ",
            "  ***  "
        ]

    def print_pattern(self):
        for line in self.pattern:
            print(line)

if __name__ == '__main__':
    heart = HeartPattern()
    heart.print_pattern()