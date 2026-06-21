class LogicalEvaluator:
    def evaluate(self, expression):
        if isinstance(expression, bool):
            return expression
        elif isinstance(expression, dict):
            return {k: self.evaluate(v) for k, v in expression.items()}
        elif isinstance(expression, list):
            return [self.evaluate(item) for item in expression]
        elif isinstance(expression, str):
            if expression == "True":
                return True
            elif expression == "False":
                return False

def nested_logic_test():
    evaluator = LogicalEvaluator()
    
    test_cases = [
        (True and False or True, True),
        ((not True) or False, False),
        (True and (not False), True),
        (False or (True and not True), False)
    ]
    
    for i, (expr, expected) in enumerate(test_cases):
        actual = evaluator.evaluate(expr)
        print(f"Case {i+1}: Expression = {expr}, Expected = {expected}, Actual = {actual}")

if __name__ == '__main__':
    nested_logic_test()