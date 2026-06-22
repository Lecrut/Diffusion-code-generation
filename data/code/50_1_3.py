class TrianglePattern:
    def __init__(self, height):
        if not isinstance(height, int):
            raise TypeError("Height must be an integer")
        if height < 1:
            raise ValueError("Height must be at least 1")
        self.height = height

    def get_rows(self):
        rows = []
        for i in range(1, self.height + 1):
            width = 2 * i - 1
            total_width = 2 * self.height - 1
            padding = (total_width - width) // 2
            row_str = ' ' * padding + '*' * width
            rows.append(row_str)
        return rows

    def render(self):
        rows = self.get_rows()
        return '\n'.join(rows)

if __name__ == '__main__':
    height_value = 7
    pattern = TrianglePattern(height_value)
    print(pattern.render())