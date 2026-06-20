class LogicalEvaluator:
    TRUE_VALUES = {'True', 'true'}
    FALSE_VALUES = {'False', 'false'}

    @staticmethod
    def is_true(statement):
        return statement in LogicalEvaluator.TRUE_VALUES

    @staticmethod
    def is_false(statement):
        return statement in LogicalEvaluator.FALSE_VALUES

if __name__ == '__main__':
    sample_statements = [
        "True",
        "False",
        "not True",
        "not False",
        "True and True",
        "True and False",
        "False and True",
        "False and False",
        "True or True",
        "True or False",
        "False or True",
        "False or False"
    ]

    evaluator = LogicalEvaluator()
    results = [evaluator.is_true(statement) for statement in sample_statements]
    print(results)