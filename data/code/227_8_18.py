class HeartPatternPrinter:
    HEART_PATTERN = [
        "  *****",
        " **   *",
        "*     *",
        "*     *",
        " *   * ",
        "  ***  "
    ]

    @staticmethod
    def print_pattern():
        for line in HeartPatternPrinter.HEART_PATTERN:
            print(line)

if __name__ == '__main__':
    HeartPatternPrinter.print_pattern()