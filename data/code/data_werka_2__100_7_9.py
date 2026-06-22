class LogicalConditionEvaluator:
    def __init__(self, threshold: int = 10, multiplier: float = 1.5):
        self.threshold = threshold
        self.multiplier = multiplier

    def evaluate(self, x: int, y: str, z: float) -> bool:
        if not isinstance(x, int):
            raise ValueError("x must be an integer")
        if not isinstance(y, str):
            raise ValueError("y must be a string")
        if not isinstance(z, float):
            raise ValueError("z must be a float")
        
        base_check = x > self.threshold
        string_check = len(y) >= 3 and y.isalnum()
        value_check = z * self.multiplier > 20.0
        
        if base_check:
            return string_check and value_check
        else:
            return not string_check or not value_check

    def get_status(self, x: int, y: str, z: float) -> str:
        result = self.evaluate(x, y, z)
        if result:
            return "PASS"
        return "FAIL"

if __name__ == '__main__':
    evaluator = LogicalConditionEvaluator(threshold=5, multiplier=2.0)
    val_x = 10
    val_y = "abc123"
    val_z = 10.0
    outcome = evaluator.evaluate(val_x, val_y, val_z)
    status = evaluator.get_status(val_x, val_y, val_z)
    print(outcome)
    print(status)