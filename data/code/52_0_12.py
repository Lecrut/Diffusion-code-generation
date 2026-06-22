class DiamondGenerator:
    def __init__(self, size: int):
        self.size = size
        self._lines = []

    def _calculate_upper_half(self):
        upper = []
        mid = self.size // 2
        for i in range(mid + 1):
            spaces = ' ' * (mid - i)
            stars = '*' * (2 * i + 1)
            upper.append(spaces + stars)
        return upper

    def _calculate_lower_half(self, upper: list):
        lower = []
        for line in reversed(upper[:-1]):
            lower.append(line)
        return lower

    def render(self) -> list:
        if self.size <= 0:
            return []
        upper = self._calculate_upper_half()
        lower = self._calculate_lower_half(upper)
        self._lines = upper + lower
        return self._lines

    def get_line_count(self) -> int:
        return len(self._lines)

    def get_center_star_count(self) -> int:
        if not self._lines:
            return 0
        mid_idx = self.size // 2
        line = self._lines[mid_idx]
        stripped = line.strip()
        return len(stripped)

if __name__ == '__main__':
    generator = DiamondGenerator(5)
    pattern = generator.render()
    for line in pattern:
        print(line)
    print(generator.get_line_count())
    print(generator.get_center_star_count())