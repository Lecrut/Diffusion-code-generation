class StatusEvaluator:
    def __init__(self, thresholds):
        self.thresholds = thresholds

    def evaluate_status(self, value):
        return (
            "Critical"
            if value < self.thresholds["critical"]
            else "Warning"
            if value < self.thresholds["warning"]
            else "Normal"
        )

if __name__ == '__main__':
    evaluator = StatusEvaluator({"critical": 10, "warning": 50})
    print(evaluator.evaluate_status(3))
    print(evaluator.evaluate_status(20))
    print(evaluator.evaluate_status(75))