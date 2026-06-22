class TruthTableGenerator:
    def __init__(self):
        self.var_names = ['A', 'B', 'C']
        self.num_vars = len(self.var_names)
        self.total_rows = 1 << self.num_vars

    def generate(self):
        rows = []
        header = ' | '.join(self.var_names) + ' | F'
        rows.append(header)
        rows.append('-' * len(header))
        
        for index in range(self.total_rows):
            bits = []
            for pos in range(self.num_vars - 1, -1, -1):
                mask = 1 << pos
                val = bool(index & mask)
                bits.append(val)
            
            f_val = bits[0] and bits[1] and bits[2]
            
            row_parts = [str(int(b)) for b in bits]
            row_parts.append(str(int(f_val)))
            row_str = ' | '.join(row_parts)
            rows.append(row_str)
        
        return '\n'.join(rows)

if __name__ == '__main__':
    generator = TruthTableGenerator()
    output = generator.generate()
    print(output)