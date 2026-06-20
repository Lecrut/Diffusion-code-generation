class TruthTableGenerator:
    def __init__(self, conditions):
        self.conditions = conditions
        self.num_conditions = len(conditions)
        self.num_rows = 2 ** self.num_conditions

    def generate_truth_table(self):
        print(f"Truth Table for {' and '.join(self.conditions)}:")
        for i in range(self.num_rows):
            row_values = []
            for j in range(self.num_conditions):
                if (i >> j) & 1:
                    row_values.append('1')
                else:
                    row_values.append('0')
            print(" ".join(row_values))

if __name__ == '__main__':
    generator = TruthTableGenerator(['P', 'Q'])
    generator.generate_truth_table()