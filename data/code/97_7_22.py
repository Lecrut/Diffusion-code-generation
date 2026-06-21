class TruthTableGenerator:
    def __init__(self, variable_names=None, num_vars=None):
        if variable_names is not None and num_vars is not None:
            raise ValueError("Provide either variable_names or num_vars, not both.")
        if variable_names is None and num_vars is None:
            raise ValueError("Must provide either variable_names or num_vars.")
        if variable_names is not None:
            if not isinstance(variable_names, list) or not all(isinstance(v, str) for v in variable_names):
                raise ValueError("variable_names must be a list of strings.")
            self.num_vars = len(variable_names)
            self.variables = list(variable_names)
        else:
            if not isinstance(num_vars, int) or num_vars < 0:
                raise ValueError("num_vars must be a non-negative integer.")
            self.num_vars = num_vars
            self.variables = [f"p{i+1}" for i in range(num_vars)]

    def generate(self):
        if self.num_vars == 0:
            return [], []
        
        total_rows = 2 ** self.num_vars
        headers = self.variables
        rows = []
        
        for i in range(total_rows):
            row = []
            for j in range(self.num_vars - 1, -1, -1):
                bit = (i >> j) & 1
                row.append(bool(bit))
            rows.append(row)
        
        return headers, rows

if __name__ == '__main__':
    generator = TruthTableGenerator(variable_names=['X', 'Y', 'Z'])
    headers, rows = generator.generate()
    print(headers)
    for row in rows:
        print(row)