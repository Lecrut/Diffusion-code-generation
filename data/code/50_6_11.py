class StarTriangle:
    def __init__(self, h):
        self._h = h
        self._max_width = 2 * h - 1

    def _get_line(self, i):
        width = 2 * i - 1
        padding = (self._max_width - width) // 2
        return ' ' * padding + '*' * width

    def render(self):
        lines = [self._get_line(i) for i in range(1, self._h + 1)]
        for i in range(self._h - 1, 0, -1):
            lines.append(self._get_line(i))
        return '\n'.join(lines)

if __name__ == '__main__':
    tri = StarTriangle(6)
    result = tri.render()
    print(result)
    print(len(result.splitlines()))
    print(len(result))