import re

class LogicEvaluator:
    VARIABLES_PATTERN = r'[A-Za-z_]\w*'

    @staticmethod
    def parse_statements(text):
        return re.findall(r"if\s+(.*?):\s*(.*)", text, re.DOTALL)

    @staticmethod
    def extract_variables(condition):
        return set(re.findall(LogicEvaluator.VARIABLES_PATTERN, condition))

    @staticmethod
    def evaluate_expression(condition, assignments):
        exec(f'assign = {condition}', assignments)
        return 'assign'

    @staticmethod
    def check_contradictions(statements):
        variables = set()
        for _, condition in statements:
            variables.update(LogicEvaluator.extract_variables(condition))
        
        num_vars = len(variables)
        for assignment_tuple in product([False, True], repeat=num_vars):
            assignments = dict(zip(variables, assignment_tuple))
            results = [LogicEvaluator.evaluate_expression(cond, assignments) for cond, _ in statements]
            if all(results) or all(not result for result in results):
                return False
        return True

if __name__ == '__main__':
    sample_string_1 = "if x > 5: print('A')"
    sample_string_2 = "if y < 10 and z > 20: print('B')"
    sample_string_3 = "if a > 10 and a < 5: print('C')"
    sample_string_4 = "if x > 5 and not (x > 5): print('D')"
    sample_string_5 = "if p or q: print('E')"

    evaluator = LogicEvaluator()
    statements_1 = LogicEvaluator.parse_statements(sample_string_1)
    statements_2 = LogicEvaluator.parse_statements(sample_string_2)
    statements_3 = LogicEvaluator.parse_statements(sample_string_3)
    statements_4 = LogicEvaluator.parse_statements(sample_string_4)
    statements_5 = LogicEvaluator.parse_statements(sample_string_5)

    print(LogicEvaluator.check_contradictions(statements_1))
    print(LogicEvaluator.check_contradictions(statements_2))
    print(LogicEvaluator.check_contradictions(statements_3))
    print(LogicEvaluator.check_contradictions(statements_4))
    print(LogicEvaluator.check_contradictions(statements_5))