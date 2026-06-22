class Checkerboard:
    SYMBOL_X = 'X'
    SYMBOL_DOT = '.'
    
    @staticmethod
    def generate(size):
        pattern = []
        for i in range(size):
            row = []
            for j in range(size):
                if (i + j) % 2 == 0:
                    row.append(Checkerboard.SYMBOL_X)
                else:
                    row.append(Checkerboard.SYMBOL_DOT)
            pattern.append(''.join(row))
        return '\n'.join(pattern)

if __name__ == '__main__':
    checkerboard = Checkerboard.generate(4)
    print(checkerboard)