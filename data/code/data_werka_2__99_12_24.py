class FlagEvaluator:
    def __init__(self, flags: dict):
        self.flags = flags

    def evaluate(self, expression: str) -> bool:
        if not isinstance(expression, str):
            raise ValueError("Expression must be a string")
        
        cleaned = expression.replace(" ", "")
        if not cleaned:
            raise ValueError("Empty expression")
            
        return self._parse_or(cleaned)

    def _parse_or(self, expr: str) -> bool:
        parts = expr.split('|')
        results = []
        for part in parts:
            results.append(self._parse_and(part))
            if results[-1]:
                return True
        return any(results)

    def _parse_and(self, expr: str) -> bool:
        parts = expr.split('&')
        results = []
        for part in parts:
            results.append(self._parse_not(part))
            if not results[-1]:
                return False
        return all(results)

    def _parse_not(self, expr: str) -> bool:
        if expr.startswith('~'):
            return not self._parse_not(expr[1:])
        return self._parse_atom(expr)

    def _parse_atom(self, expr: str) -> bool:
        if expr.startswith('(') and expr.endswith(')'):
            return self._parse_or(expr[1:-1])
        
        if expr in self.flags:
            return bool(self.flags[expr])
        
        raise ValueError(f"Unknown flag: {expr}")

if __name__ == '__main__':
    flags = {
        'A': True,
        'B': False,
        'C': True,
        'D': False
    }
    
    evaluator = FlagEvaluator(flags)
    
    result1 = evaluator.evaluate("A & B | C")
    print(result1)
    
    result2 = evaluator.evaluate("~B & A")
    print(result2)
    
    result3 = evaluator.evaluate("A & (B | D)")
    print(result3)