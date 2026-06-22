class DiamondPattern:
    def __init__(self, radius):
        self.radius = radius

    def get_rows(self):
        rows = []
        r = self.radius
        for i in range(r, 0, -1):
            spaces = " " * (r - i)
            stars = "* " * i
            rows.append(spaces + stars.strip())
        for i in range(1, r + 1):
            spaces = " " * (r - i)
            stars = "* " * i
            rows.append(spaces + stars.strip())
        return rows

if __name__ == '__main__':
    pattern = DiamondPattern(4)
    result = pattern.get_rows()
    for line in result:
        print(line)