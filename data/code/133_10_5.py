class LogicEvaluator:
    def __init__(self):
        self.logic_map = {
            'A': True,
            'B': False,
            'C': True,
            'D': False,
            'E': (True and False) or (not True),
            'F': (False and True) or (not False)
        }

    def evaluate_nested_logic(self):
        result = (
            self.logic_map['A'] and self.logic_map['B']
        ) or (
            not self.logic_map['C'] and self.logic_map['D']
        ) or (
            self.logic_map['E'] and self.logic_map['F']
        )
        return result

if __name__ == '__main__':
    evaluator = LogicEvaluator()
    print(evaluator.evaluate_nested_logic())