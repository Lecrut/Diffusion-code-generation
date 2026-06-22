class LogicalConditionEvaluator:
    def __init__(self, threshold: int, multiplier: float, suffix: str):
        self.threshold = threshold
        self.multiplier = multiplier
        self.suffix = suffix

    def evaluate(self, value: int, text: str, flag: bool) -> bool:
        if not isinstance(value, int):
            raise ValueError("value must be an integer")
        if not isinstance(text, str):
            raise ValueError("text must be a string")
        if not isinstance(flag, bool):
            raise ValueError("flag must be a boolean")
        
        base_check = value > self.threshold
        text_check = text.endswith(self.suffix)
        flag_check = flag is True
        
        if base_check:
            if text_check:
                return flag_check
            else:
                return value * self.multiplier > 50.0
        else:
            return not flag_check and len(text) > 0

if __name__ == '__main__':
    evaluator = LogicalConditionEvaluator(threshold=10, multiplier=2.5, suffix="ing")
    result1 = evaluator.evaluate(15, "running", True)
    result2 = evaluator.evaluate(5, "walk", False)
    result3 = evaluator.evaluate(20, "jump", False)
    print(result1)
    print(result2)
    print(result3)