from typing import Callable, Any
def evaluate_logic(condition: bool) -> bool:
    return condition
class ComplexLogicEvaluator:
    def __init__(self):
        self.conditions = []
    def add_condition(self, func: Callable[[bool], bool]) -> None:
        if not callable(func) or isinstance(func, type(ComplexLogicEvaluator)):
            raise TypeError("Must provide a valid callable.")
        self.conditions.append(func)
    def run(self, *args: Any) -> bool:
        results = [cond(*args) for cond in self.conditions]
        return reduce(lambda x, y: x or y, results, False)
def main() -> None:
    evaluator = ComplexLogicEvaluator()
    def condition_a(x: int) -> bool:
        if x > 10:
            return True
        else:
            return False
    def condition_b(y: str) -> bool:
        if len(y) >= 5 and y.isalpha():
            return True
        else:
            return False
    evaluator.add_condition(condition_a)
    evaluator.add_condition(condition_b)
    sample_x = 12
    sample_y = "hello"
    final_result = evaluator.run(sample_x, sample_y)
    if __name__ == '__main__':
        print(final_result)