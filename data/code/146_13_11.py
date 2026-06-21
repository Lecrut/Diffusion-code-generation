class DecisionEvaluator:
    HIGH_THRESHOLD = 20
    LOW_THRESHOLD = 5

    @staticmethod
    def evaluate_conditions(value1, value2, value3=None):
        if value1 > 10 and value2 < DecisionEvaluator.LOW_THRESHOLD:
            return "Condition A met"
        elif value1 <= 10 and value2 >= DecisionEvaluator.LOW_THRESHOLD:
            if value3 is not None and value3 > DecisionEvaluator.HIGH_THRESHOLD:
                return "Condition B met (High)"
            else:
                return "Condition B met (Low)"
        elif value1 > DecisionEvaluator.LOW_THRESHOLD and value2 > 15:
            return "Condition C met"
        else:
            return "Default Condition"

if __name__ == '__main__':
    evaluator = DecisionEvaluator()
    data1 = 12
    data2 = 3
    data3 = 15
    print(evaluator.evaluate_conditions(data1, data2, data3))