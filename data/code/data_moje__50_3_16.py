class StarTriangleBuilder:
    def __init__(self, row_count):
        self.row_count = row_count
        self.lines = []
    
    def build(self):
        for i in range(1, self.row_count + 1):
            line = '*' * i
            self.lines.append(line)
            print(line)
    
    def get_total_lines(self):
        return len(self.lines)
    
    def get_last_line_length(self):
        if not self.lines:
            return 0
        return len(self.lines[-1])

if __name__ == '__main__':
    TARGET_ROWS = 15
    builder = StarTriangleBuilder(TARGET_ROWS)
    builder.build()
    print(builder.get_total_lines())
    print(builder.get_last_line_length())