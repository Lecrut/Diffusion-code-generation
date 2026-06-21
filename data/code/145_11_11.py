class AccessControl:
    def __init__(self, inputs):
        self.inputs = inputs

    def evaluate_expression(self, expression):
        try:
            result = eval(expression, {"__builtins__": None}, self.inputs)
            return bool(result)
        except Exception:
            return None

if __name__ == '__main__':
    boolean_inputs = {
        "A": True,
        "B": False,
        "C": True,
        "D": False
    }
    access_control = AccessControl(boolean_inputs)
    
    expressions = [
        "(A and B) or C",
        "not A",
        "B and D",
        "C or not B"
    ]
    
    for expr in expressions:
        result = access_control.evaluate_expression(expr)
        print(f"{expr}: {result}")