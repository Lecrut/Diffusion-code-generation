class TruthTableGenerator:
    INPUT_KEYS = ['a', 'b']
    OUTPUT_KEY = 'result'

    @staticmethod
    def generate_truth_table(expression, inputs):
        table = []
        for combination in [(False, False), (False, True), (True, False), (True, True)]:
            row = {key: value for key, value in zip(TruthTableGenerator.INPUT_KEYS, combination)}
            row[TruthTableGenerator.OUTPUT_KEY] = eval(expression, {"__builtins__": None}, row)
            table.append(row)
        return table

if __name__ == '__main__':
    generator = TruthTableGenerator()
    sample_expression = 'a and b'
    truth_table = generator.generate_truth_table(sample_expression, TruthTableGenerator.INPUT_KEYS)
    print(truth_table)