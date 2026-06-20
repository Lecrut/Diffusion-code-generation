class StatementEvaluator:
    TRUE_VALUES = {'true', 'True'}
    FALSE_VALUES = {'false', 'False'}

    @staticmethod
    def is_true(statement):
        return statement in StatementEvaluator.TRUE_VALUES

    @staticmethod
    def is_false(statement):
        return statement in StatementEvaluator.FALSE_VALUES

if __name__ == '__main__':
    statements = ["true", "false", "True", "False", "2 + 2 == 4", "3 > 5"]
    results = []
    for statement in statements:
        if StatementEvaluator.is_true(statement):
            results.append(True)
        elif StatementEvaluator.is_false(statement):
            results.append(False)
        else:
            print(f"Error: Invalid value encountered: '{statement}'")
            exit(1)

    print(results)