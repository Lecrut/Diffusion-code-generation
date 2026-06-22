class TruthTableGenerator:
    def __init__(self, variable_names):
        if not variable_names:
            raise ValueError("Variable names list cannot be empty")
        self.variable_names = list(variable_names)
        self.num_vars = len(self.variable_names)
        self.total_rows = 2 ** self.num_vars

    def _generate_bits(self, row_index):
        bits = []
        for i in range(self.num_vars - 1, -1, -1):
            bit = (row_index >> i) & 1
            bits.append(bool(bit))
        return bits

    def get_rows(self):
        rows = []
        for i in range(self.total_rows):
            bits = self._generate_bits(i)
            row_dict = {}
            for j, var_name in enumerate(self.variable_names):
                row_dict[var_name] = bits[j]
            rows.append(row_dict)
        return rows

    def get_headers(self):
        return self.variable_names

    def format_table(self):
        headers = self.get_headers()
        rows = self.get_rows()
        col_widths = [len(h) for h in headers]
        for row in rows:
            for var_name in headers:
                val_str = str(row[var_name])
                if len(val_str) > col_widths[headers.index(var_name)]:
                    col_widths[headers.index(var_name)] = len(val_str)
        
        header_line = " | ".join(h.ljust(col_widths[i]) for i, h in enumerate(headers))
        sep_line = "-+-".join("-" * w for w in col_widths)
        
        lines = [header_line, sep_line]
        for row in rows:
            row_line = " | ".join(str(row[h]).ljust(col_widths[i]) for i, h in enumerate(headers))
            lines.append(row_line)
        return "\n".join(lines)

if __name__ == '__main__':
    generator = TruthTableGenerator(['P', 'Q', 'R'])
    print(generator.format_table())
    print(generator.get_rows())
    print(generator.get_headers())