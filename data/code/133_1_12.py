class StatementEvaluator:
    TRUE = 'True'
    FALSE = 'False'

    @staticmethod
    def evaluate(statement):
        return eval(statement)

if __name__ == '__main__':
    sample_statements = [
        StatementEvaluator.TRUE,
        StatementEvaluator.FALSE,
        '2 + 2 == 4',
        '3 > 5',
        "'hello' == 'world'",
        "not False",
        "len([1, 2, 3]) > 2"
    ]
    results = {statement: StatementEvaluator.evaluate(statement) for statement in sample_statements}
    print(results)