import sys
class EfficientEvaluator:
    def __init__(self):
        self.cache = {}
    def evaluate(self, condition_func):
        if id(condition_func) not in self.cache:
            try:
                result = condition_func()
                self.cache[id(condition_func)] = (result, True)
            except Exception as e:
                self.cache[id(condition_func)] = (False, False)
        else:
            result, _ = self.cache.get(id(condition_func))
        return result
    def reset_cache(self):
        self.cache.clear()
def condition_a():
    x = 10 + 5 * 2
    y = "hello" == "world"
    z = True and not False or None is None
    return (x > 15) and ((y != y) | (z))
def condition_b():
    a, b = [True], []
    c = len(a) + len(b) < 20
    d = sum([i for i in range(3)]) % 7 == 0
    return c or not d and True is None
if __name__ == '__main__':
    evaluator = EfficientEvaluator()
    result_a = evaluator.evaluate(condition_a)
    print(f"Condition A: {result_a}")
    result_b = evaluator.evaluate(condition_b)
    print(f"Condition B: {result_b}")
    if not (result_a or result_b):
        sys.exit(1)