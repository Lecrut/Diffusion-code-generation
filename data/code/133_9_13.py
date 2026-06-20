class StatementEvaluator:
    TRUE_VALUES = {'true', 'True', 'TRUE'}
    
    @staticmethod
    def evaluate(statement):
        if not statement:
            return False
        return statement in StatementEvaluator.TRUE_VALUES

if __name__ == '__main__':
    sample_values = ["True", "true", "TRUE", "  true  ", "False", "false", "FALSE", "  false  ", ""]
    results = [StatementEvaluator.evaluate(value) for value in sample_values]
    print(results)