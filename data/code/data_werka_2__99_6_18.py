from typing import List, Tuple, Union

PRECEDENCE_MAP = {
    'OR': 1,
    'AND': 2,
    'NOT': 3
}

OPERATOR_MAP = {
    'OR': lambda a, b: a or b,
    'AND': lambda a, b: a and b,
    'NOT': lambda a: not a
}

VALID_TOKENS = {'TRUE', 'FALSE', 'AND', 'OR', 'NOT', '(', ')'}

def _tokenize(expression: str) -> List[str]:
    cleaned = expression.strip()
    if not cleaned:
        raise ValueError("Empty expression provided")
    parts = cleaned.split()
    for part in parts:
        if part not in VALID_TOKENS:
            raise ValueError(f"Invalid token: {part}")
    return parts

def _parse_postfix(tokens: List[str]) -> List[str]:
    output_queue: List[str] = []
    operator_stack: List[str] = []
    for token in tokens:
        if token in ('TRUE', 'FALSE'):
            output_queue.append(token)
        elif token == '(':
            operator_stack.append(token)
        elif token == ')':
            while operator_stack and operator_stack[-1] != '(':
                output_queue.append(operator_stack.pop())
            if not operator_stack:
                raise ValueError("Mismatched parentheses")
            operator_stack.pop()
        elif token == 'NOT':
            operator_stack.append(token)
        else:
            while (operator_stack and 
                   operator_stack[-1] != '(' and 
                   PRECEDENCE_MAP.get(operator_stack[-1], 0) >= PRECEDENCE_MAP.get(token, 0)):
                output_queue.append(operator_stack.pop())
            operator_stack.append(token)
    while operator_stack:
        top = operator_stack.pop()
        if top == '(':
            raise ValueError("Mismatched parentheses")
        output_queue.append(top)
    return output_queue

def _evaluate_postfix(postfix_expr: List[str]) -> bool:
    stack: List[bool] = []
    for token in postfix_expr:
        if token == 'TRUE':
            stack.append(True)
        elif token == 'FALSE':
            stack.append(False)
        elif token == 'NOT':
            if len(stack) < 1:
                raise ValueError("Invalid expression structure")
            val = stack.pop()
            stack.append(not val)
        else:
            if len(stack) < 2:
                raise ValueError("Invalid expression structure")
            right = stack.pop()
            left = stack.pop()
            stack.append(OPERATOR_MAP[token](left, right))
    if len(stack) != 1:
        raise ValueError("Invalid expression structure")
    return stack[0]

def analyze_boolean_expression(expression: str) -> dict:
    tokens = _tokenize(expression)
    postfix = _parse_postfix(tokens)
    result = _evaluate_postfix(postfix)
    return {
        "original": expression,
        "postfix": postfix,
        "result": result
    }

if __name__ == '__main__':
    test_cases = [
        "TRUE OR FALSE",
        "TRUE AND FALSE",
        "NOT TRUE",
        "TRUE AND (FALSE OR TRUE)",
        "NOT (TRUE AND FALSE)"
    ]
    for expr in test_cases:
        try:
            analysis = analyze_boolean_expression(expr)
            print(f"Expression: {analysis['original']}")
            print(f"Postfix: {analysis['postfix']}")
            print(f"Result: {analysis['result']}")
            print("-" * 20)
        except ValueError as e:
            print(f"Error in '{expr}': {e}")
            print("-" * 20)