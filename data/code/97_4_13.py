TRUTH_TABLE_FORMAT = "{P} | {Q} | {P_IMPLIES_Q}"

class TruthTableGenerator:
    def generate_truth_table(self):
        table_entries = []
        for P in [False, True]:
            for Q in [False, True]:
                result = not P or Q
                table_entries.append(TRUTH_TABLE_FORMAT.format(P=P, Q=Q, P_IMPLIES_Q=result))
        return table_entries

if __name__ == '__main__':
    generator = TruthTableGenerator()
    truth_table = generator.generate_truth_table()
    for entry in truth_table:
        print(entry)