class FlagEvaluator:
    def __init__(self):
        self.flags = {}

    def set_flag(self, name, value):
        if not isinstance(name, str):
            raise ValueError("Flag name must be a string")
        self.flags[name] = bool(value)

    def evaluate_expression(self, expr):
        if not isinstance(expr, str):
            raise ValueError("Expression must be a string")
        
        cleaned = expr.replace(" ", "")
        
        if not cleaned:
            raise ValueError("Empty expression")
            
        return self._parse_or(cleaned)

    def _parse_or(self, expr):
        terms = self._split_by_operator(expr, '|')
        results = []
        for term in terms:
            results.append(self._parse_and(term))
            
        short_circuit = False
        for res in results:
            if res:
                short_circuit = True
                break
        return short_circuit

    def _parse_and(self, expr):
        terms = self._split_by_operator(expr, '&')
        results = []
        for term in terms:
            results.append(self._parse_not(term))
            
        short_circuit = True
        for res in results:
            if not res:
                short_circuit = False
                break
        return short_circuit

    def _parse_not(self, expr):
        if expr.startswith('!'):
            inner = self._parse_not(expr[1:])
            return not inner
        return self._parse_paren(expr)

    def _parse_paren(self, expr):
        if expr.startswith('(') and expr.endswith(')'):
            return self._parse_or(expr[1:-1])
        return self._get_flag_value(expr)

    def _get_flag_value(self, name):
        if name not in self.flags:
            raise ValueError(f"Unknown flag: {name}")
        return self.flags[name]

    def _split_by_operator(self, expr, op):
        parts = []
        current = []
        depth = 0
        i = 0
        while i < len(expr):
            char = expr[i]
            if char == '(':
                depth += 1
                current.append(char)
            elif char == ')':
                depth -= 1
                current.append(char)
            elif char == op and depth == 0:
                parts.append(''.join(current))
                current = []
            else:
                current.append(char)
            i += 1
        parts.append(''.join(current))
        return parts

if __name__ == '__main__':
    evaluator = FlagEvaluator()
    evaluator.set_flag("A", True)
    evaluator.set_flag("B", False)
    evaluator.set_flag("C", True)
    
    result1 = evaluator.evaluate_expression("A & B")
    print(result1)
    
    result2 = evaluator.evaluate_expression("A | B")
    print(result2)
    
    result3 = evaluator.evaluate_expression("!A & C")
    print(result3)
    
    result4 = evaluator.evaluate_expression("(A | B) & C")
    print(result4)