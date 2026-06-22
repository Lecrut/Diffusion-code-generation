class HollowSquareBuilder:
    def __init__(self, delimiter='*'):
        self.delimiter = delimiter

    def build(self, size):
        if size <= 0:
            return ""
        
        def row_generator():
            if size <= 2:
                yield self.delimiter * size
                return
            
            first_row = self.delimiter * size
            yield first_row
            
            for _ in range(size - 2):
                inner = self.delimiter + ' ' * (size - 2) + self.delimiter
                yield inner
            
            yield self.delimiter * size
        
        rows = list(row_generator())
        return '\n'.join(rows)

if __name__ == '__main__':
    builder = HollowSquareBuilder('#')
    result = builder.build(5)
    print(result)