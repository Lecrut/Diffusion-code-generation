class ConditionalStatement:
    def __init__(self, condition):
        self.condition = condition
    def to_symbolic_form(self):
        if isinstance(self.condition, tuple):
            return self.condition
        elif isinstance(self.condition, str):
            return {"type": "literal", "value": self.condition}
        elif isinstance(self.condition, dict):
            return self.condition
        else:
            return {"type": "unknown", "data": self.condition}
if __name__ == '__main__':
    condition1 = (10 > 5) and (2 * 3 == 6)
    cs1 = ConditionalStatement(condition1)
    symbolic1 = cs1.to_symbolic_form()
    print("Symbolic Form 1:", symbolic1)
    condition2 = "x > 0 and y < 10"
    cs2 = ConditionalStatement(condition2)
    symbolic2 = cs2.to_symbolic_form()
    print("Symbolic Form 2:", symbolic2)
    condition3 = {"a": 1, "b": 2}
    cs3 = ConditionalStatement(condition3)
    symbolic3 = cs3.to_symbolic_form()
    print("Symbolic Form 3:", symbolic3)