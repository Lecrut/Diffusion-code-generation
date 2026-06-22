import re
from typing import List, Tuple, Any

class BooleanEvaluator:
    def check_precedence(self, expression_string: str) -> List[Tuple[str, str, int]]:
        tokens = self._tokenize(expression_string)
        if not tokens:
            return []
        
        precedence_map = {
            '(': 0,
            ')': 0,
            'OR': 1,
            'AND': 2,
            'NOT': 3,
        }
        
        operators = []
        results = []
        last_was_operand = False
        
        for token in tokens:
            if token in ('AND', 'OR', 'NOT'):
                current_prec = precedence_map[token]
                
                while operators and operators[-1] != '(':
                    top_prec = precedence_map[operators[-1]]
                    if top_prec >= current_prec:
                        op = operators.pop()
                        results.append((op, token, current_prec))
                    else:
                        break
                
                operators.append(token)
                last_was_operand = False
            elif token == '(':
                operators.append(token)
                last_was_operand = False
            elif token == ')':
                while operators and operators[-1] != '(':
                    op = operators.pop()
                    results.append((op, token, precedence_map[op]))
                if operators and operators[-1] == '(':
                    operators.pop()
                last_was_operand = True
            else:
                if not last_was_operand and operators and operators[-1] == 'NOT':
                    op = operators.pop()
                    results.append((op, token, precedence_map[op]))
                last_was_operand = True
        
        while operators:
            op = operators.pop()
            if op != '(':
                results.append((op, 'END', precedence_map[op]))
        
        return results

    def _tokenize(self, expression_string: str) -> List[str]:
        pattern = r'\s*(AND|OR|NOT|\(|\)|\b(?:True|False)\b)\s*'
        parts = re.split(pattern, expression_string)
        tokens = [p for p in parts if p]
        return tokens

if __name__ == '__main__':
    evaluator = BooleanEvaluator()
    expr = "True AND False OR NOT True"
    result = evaluator.check_precedence(expr)
    print(result)
    
    expr2 = "(True OR False) AND NOT False"
    result2 = evaluator.check_precedence(expr2)
    print(result2)