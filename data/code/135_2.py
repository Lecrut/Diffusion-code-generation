class ConditionalStatement:
    def __init__(self, condition):
        self.condition = condition
    def to_symbolic_form(self):
        if isinstance(self.condition, str):
            return {"type": "literal", "value": self.condition}
        elif isinstance(self.condition, dict):
            return self._recursive_symbolic_form(self.condition)
        else:
            return {"type": "unknown", "value": self.condition}
    def _recursive_symbolic_form(self, node):
        if isinstance(node, dict):
            result = {"type": "expression"}
            for key, value in node.items():
                if key == "if":
                    result["if"] = self._recursive_symbolic_form(value)
                elif key == "and":
                    result["and"] = self._recursive_symbolic_form(value)
                elif key == "or":
                    result["or"] = self._recursive_symbolic_form(value)
                elif key == "gt":
                    result["op"] = "gt"
                    result["left"] = self._recursive_symbolic_form(value["left"])
                    result["right"] = self._recursive_symbolic_form(value["right"])
                elif key == "eq":
                    result["op"] = "eq"
                    result["left"] = self._recursive_symbolic_form(value["left"])
                    result["right"] = self._recursive_symbolic_form(value["right"])
                else:
                    result[key] = self._recursive_symbolic_form(value)
            return result
        elif isinstance(node, list):
            return [self._recursive_symbolic_form(item) for item in node]
        else:
            return {"type": "literal", "value": node}
if __name__ == '__main__':
    condition1 = {
        "op": "gt",
        "left": 10,
        "right": 5
    }
    statement1 = ConditionalStatement(condition1)
    symbolic1 = statement1.to_symbolic_form()
    print("--- Statement 1 ---")
    print(f"Original Condition: {condition1}")
    print(f"Symbolic Form: {symbolic1}")
    condition2 = {
        "op": "and",
        "left": {
            "op": "eq",
            "left": 5,
            "right": 5
        },
        "right": {
            "op": "gt",
            "left": 1,
            "right": 0
        }
    }
    statement2 = ConditionalStatement(condition2)
    symbolic2 = statement2.to_symbolic_form()
    print("\n--- Statement 2 ---")
    print(f"Original Condition: {condition2}")
    print(f"Symbolic Form: {symbolic2}")
    condition3 = "x > 5 and y == 10"
    statement3 = ConditionalStatement(condition3)
    symbolic3 = statement3.to_symbolic_form()
    print("\n--- Statement 3 ---")
    print(f"Original Condition: {condition3}")
    print(f"Symbolic Form: {symbolic3}")