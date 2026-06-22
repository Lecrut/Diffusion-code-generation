class DiamondPattern:
    SIZE = 8

    @staticmethod
    def _build_line(mid, current_idx):
        spaces = mid - current_idx
        stars = 2 * current_idx + 1
        return " " * spaces + "*" * stars

    def generate(self):
        lines = []
        mid = self.SIZE
        for i in range(mid):
            lines.append(self._build_line(mid, i))
        for i in range(mid - 2, -1, -1):
            lines.append(self._build_line(mid, i))
        return "\n".join(lines)

if __name__ == '__main__':
    pattern = DiamondPattern()
    print(pattern.generate())