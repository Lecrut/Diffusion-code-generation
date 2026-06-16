import functools
class RuleInjector:
    def inject(self):
        self.rule = None
    @functools.wraps(lambda x: print(f"Rule applied: {x}"))
    def apply_rule(self, *args, **kwargs):
        if hasattr(self, 'rule'):
            return self.rule(*args, **kwargs)
class CustomEvaluator:
    def __init__(self, injector=None):
        self.injector = injector or RuleInjector()
    @functools.wraps(lambda x: print(f"Evaluator processing {x}"))
    def evaluate(self, data):
        return f"Processed value: {data}"
def rule_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Rule execution completed for input: {args}")
        return result
    return wrapper
@rule_decorator
def age_rule(age):
    if age >= 18:
        return "Adult"
    else:
        return "Minor"
if __name__ == '__main__':
    injector = RuleInjector()
    evaluator = CustomEvaluator(injector)
    test_data = [25, 10]
    for item in test_data:
        result = evaluator.evaluate(item)
    age_result = None
    if hasattr(evaluator.injector, 'rule'):
        age_result = injector.apply_rule(30)
    print(f"Age Evaluation Result: {age_result}")