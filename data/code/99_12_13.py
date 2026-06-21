class FlagEvaluator:
    def __init__(self, flags):
        self.flags = flags

    def evaluate(self, expression):
        if not isinstance(expression, str):
            raise ValueError("Expression must be a string")
        
        cleaned = expression.replace(" ", "")
        
        if not cleaned:
            raise ValueError("Empty expression")
            
        return self._parse_or(cleaned)

    def _parse_or(self, expr):
        parts = expr.split("|")
        results = []
        for part in parts:
            results.append(self._parse_and(part))
            
        for i, res in enumerate(results):
            if res:
                return True
        return False

    def _parse_and(self, expr):
        parts = expr.split("&")
        results = []
        for part in parts:
            results.append(self._parse_not(part))
            
        for res in results:
            if not res:
                return False
        return True

    def _parse_not(self, expr):
        if expr.startswith("!"):
            return not self._parse_not(expr[1:])
        return self._parse_atom(expr)

    def _parse_atom(self, expr):
        if expr.startswith("(") and expr.endswith(")"):
            return self._parse_or(expr[1:-1])
        
        if expr in self.flags:
            return bool(self.flags[expr])
        
        raise ValueError(f"Unknown flag: {expr}")

if __name__ == '__main__':
    flags = {
        "A": True,
        "B": False,
        "C": True,
        "D": False
    }
    
    evaluator = FlagEvaluator(flags)
    
    expr1 = "A & B"
    result1 = evaluator.evaluate(expr1)
    print(result1)
    
    expr2 = "A | B"
    result2 = evaluator.evaluate(expr2)
    print(result2)
    
    expr3 = "!B & C"
    result3 = evaluator.evaluate(expr3)
    print(result3)
    
    expr4 = "(A | B) & C"
    result4 = evaluator.evaluate(expr4)
    print(result4)