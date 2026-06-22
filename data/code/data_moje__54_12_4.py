class HollowSquareBuilder:
    def __init__(self, size, delimiter="#"):
        self.size = size
        self.delimiter = delimiter

    def build(self):
        if self.size <= 0:
            return []
        if self.size == 1:
            return [self.delimiter]
        top_bottom = self.delimiter * self.size
        middle_rows = (
            self.delimiter + " " * (self.size - 2) + self.delimiter
            for _ in range(self.size - 2)
        )
        return [top_bottom] + list(middle_rows) + [top_bottom]

if __name__ == "__main__":
    builder = HollowSquareBuilder(5, "#")
    lines = builder.build()
    for line in lines:
        print(line)