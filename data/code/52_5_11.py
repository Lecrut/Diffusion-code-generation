class DiamondRenderer:
    def __init__(self, size):
        if not isinstance(size, int) or size <= 0:
            raise ValueError("Size must be a positive integer")
        self.size = size
        self.half = (size + 1) // 2

    def _build_line(self, index, offset):
        stars_count = 2 * (index + 1) - 1
        spaces_count = offset - index
        if spaces_count < 0:
            spaces_count = 0
        return ' ' * spaces_count + '*' * stars_count

    def render(self):
        lines = []
        for i in range(self.half):
            lines.append(self._build_line(i, self.half - 1))
        
        start = self.half - 2 if self.half > 1 else 0
        for i in range(start, -1, -1):
            lines.append(self._build_line(i, self.half - 1))
        return '\n'.join(lines)

if __name__ == '__main__':
    result = DiamondRenderer(3).render()
    print(result)