class TruthEvaluator:
    def process_statements(self, statements):
        true_count = 0
        false_count = 0
        for statement in statements:
            if statement.lower() == 'true':
                true_count += 1
            elif statement.lower() == 'false':
                false_count += 1
        return {'True': true_count, 'False': false_count}
if __name__ == '__main__':
    evaluator = TruthEvaluator()
    sample_statements = ["True", "false", "True", "False", "true", "false"]
    results = evaluator.process_statements(sample_statements)
    print(results)