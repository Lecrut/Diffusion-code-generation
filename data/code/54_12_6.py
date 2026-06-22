class HollowSquareBuilder:
    def __init__(self, delimiter: str = '*'):
        self.delimiter = delimiter

    def build_hollow_square(self, size: int) -> str:
        if size <= 0:
            return ""
        if size == 1:
            return self.delimiter
        
        top_bottom = self.delimiter * size
        
        if size == 2:
            return top_bottom + "\n" + top_bottom
        
        middle_row = self.delimiter + (' ' * (size - 2)) + self.delimiter
        
        rows = []
        rows.append(top_bottom)
        
        middle_generator = (middle_row for _ in range(size - 2))
        for row in middle_generator:
            rows.append(row)
            
        rows.append(top_bottom)
        
        return '\n'.join(rows)

if __name__ == '__main__':
    builder = HollowSquareBuilder(delimiter='#')
    result = builder.build_hollow_square(5)
    print(result)