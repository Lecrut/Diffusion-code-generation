import itertools

class SymbolBlockBuilder:
    SYMBOL = '*'
    
    @staticmethod
    def construct_symbol_block(rows, cols):
        if rows < 1 or cols < 1:
            raise ValueError("Rows and columns must be positive integers.")
        
        block = list(itertools.product(range(rows), range(cols)))
        return '\n'.join(SymbolBlockBuilder.SYMBOL * len(row) for row in block)

if __name__ == '__main__':
    sample_block = SymbolBlockBuilder.construct_symbol_block(3, 4)
    print(sample_block)