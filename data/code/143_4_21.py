import re

class ContradictionChecker:

    @staticmethod
    def parse_statements(text):
        statements = re.findall('if\\s+(.*?):\\s*(.*)', text, re.DOTALL)
        return statements

    @staticmethod
    def evaluate_conditions(conditions):
        for condition in conditions:
            try:
                if eval(condition) != True:
                    return False
            except Exception as e:
                return False
        return True

    @staticmethod
    def check_contradictions(text1, text2):
        statements1 = ContradictionChecker.parse_statements(text1)
        statements2 = ContradictionChecker.parse_statements(text2)
        conditions1 = [condition for _, condition in statements1]
        conditions2 = [condition for _, condition in statements2]
        return not (ContradictionChecker.evaluate_conditions(conditions1) and ContradictionChecker.evaluate_conditions(conditions2))
if __name__ == '__main__':
    sample_string_1 = "if x > 5: print('A')"
    sample_string_2 = "if y < 10 and z > 20: print('B')"
    sample_string_3 = "if a > 10 and a < 5: print('C')"
    sample_string_4 = "if x > 5 and not (x > 5): print('D')"
    sample_string_5 = "if p or q: print('E')"
    result = ContradictionChecker.check_contradictions(sample_string_1, sample_string_2)
    print(result)