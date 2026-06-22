class HollowSquareBuilder:
    def __init__(self, size=5, border_char='*', fill_char=' '):
        self.size = size
        self.border_char = border_char
        self.fill_char = fill_char

    def build(self):
        if self.size <= 0:
            return []
        if self.size == 1:
            return [self.border_char]
        
        top_row = (self.border_char for _ in range(self.size))
        middle_rows = []
        
        for _ in range(self.size - 2):
            row_gen = (self.border_char if j == 0 or j == self.size - 1 else self.fill_char for j in range(self.size))
            middle_rows.append(row_gen)
        
        bottom_row = (self.border_char for _ in range(self.size))
        
        rows = [top_row]
        rows.extend(middle_rows)
        rows.append(bottom_row)
        
        return [''.join(row) for row in rows]

if __name__ == '__main__':
    builder = HollowSquareBuilder(5, '#', '.')
    result = builder.build()
    for line in result:
        print(line)
    
    builder_small = HollowSquareBuilder(3, '@', 'o')
    small_result = builder_small.build()
    for line in small_result:
        print(line)