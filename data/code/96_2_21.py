import re
from typing import Dict, Any

def evaluate_boolean_expression(expression: str, variables: Dict[str, bool]) -> bool:
    cleaned = expression.replace(' ', '')
    
    def parse_or(index: int) -> tuple:
        left, index = parse_and(index)
        while index < len(cleaned) and cleaned[index] == '|':
            index += 1
            right, index = parse_and(index)
            left = left or right
        return left, index

    def parse_and(index: int) -> tuple:
        left, index = parse_not(index)
        while index < len(cleaned) and cleaned[index] == '&':
            index += 1
            right, index = parse_not(index)
            left = left and right
        return left, index

    def parse_not(index: int) -> tuple:
        if index < len(cleaned) and cleaned[index] == '!':
            index += 1
            val, index = parse_not(index)
            return not val, index
        return parse_primary(index)

    def parse_primary(index: int) -> tuple:
        if index < len(cleaned) and cleaned[index] == '(':
            index += 1
            val, index = parse_or(index)
            if index < len(cleaned) and cleaned[index] == ')':
                index += 1
            return val, index
        if index < len(cleaned) and cleaned[index] == 'T':
            return True, index + 1
        if index < len(cleaned) and cleaned[index] == 'F':
            return False, index + 1
        
        match = re.match(r'[A-Za-z_]\w*', cleaned[index:])
        if match:
            var_name = match.group(0)
            if var_name in variables:
                return variables[var_name], index + len(var_name)
            raise ValueError(f"Unknown variable: {var_name}")
        
        raise ValueError(f"Unexpected character: {cleaned[index]}")

    result, end_index = parse_or(0)
    if end_index != len(cleaned):
        raise ValueError(f"Unexpected character at end: {cleaned[end_index:]}")
    return result

if __name__ == '__main__':
    expr = '((A and B) or C)'
    vars_map = {'A': True, 'B': False, 'C': True}
    print(evaluate_boolean_expression(expr, vars_map))