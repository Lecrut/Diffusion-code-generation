class LogicEvaluator:
    TRUE = True
    FALSE = False

    @staticmethod
    def evaluate_nested_logic():
        logic_map = {
            'A': LogicEvaluator.TRUE,
            'B': LogicEvaluator.FALSE,
            'C': LogicEvaluator.TRUE,
            'D': LogicEvaluator.FALSE,
            'E': (LogicEvaluator.TRUE and LogicEvaluator.FALSE) or (not LogicEvaluator.TRUE),
            'F': (LogicEvaluator.FALSE and LogicEvaluator.TRUE) or (not LogicEvaluator.FALSE)
        }
        result = (
            logic_map['A'] and logic_map['B']
        ) or (
            not logic_map['C'] and logic_map['D']
        ) or (
            logic_map['E'] and logic_map['F']
        )
        return result

if __name__ == '__main__':
    evaluator = LogicEvaluator()
    print(evaluator.evaluate_nested_logic())