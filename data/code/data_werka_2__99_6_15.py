from typing import List, Tuple, Union

def analyze_boolean_expression(expression: str) -> bool:
    cleaned = expression.strip()
    if not cleaned:
        raise ValueError("Empty expression")
    tokens = _tokenize(cleaned)
    if not tokens:
        raise ValueError("No tokens found")
    postfix = _infix_to_postfix(tokens)
    result = _evaluate_postfix(postfix)
    return result

def _tokenize(expr: str) -> List[str]:
    tokens = []
    current = []
    i = 0
    while i < len(expr):
        char = expr[i]
        if char == ' ':
            if current:
                tokens.append(''.join(current))
                current = []
            i += 1
            continue
        if char in '()':
            if current:
                tokens.append(''.join(current))
                current = []
            tokens.append(char)
            i += 1
            continue
        if char.isalpha():
            current.append(char)
            i += 1
            continue
        raise ValueError(f"Invalid character: {char}")
    if current:
        tokens.append(''.join(current))
    processed = []
    for tok in tokens:
        upper = tok.upper()
        if upper == 'AND':
            processed.append('AND')
        elif upper == 'OR':
            processed.append('OR')
        elif upper == 'NOT':
            processed.append('NOT')
        elif upper == 'XOR':
            processed.append('XOR')
        elif upper == 'TRUE':
            processed.append('TRUE')
        elif upper == 'FALSE':
            processed.append('FALSE')
        elif upper in ('(', ')'):
            processed.append(upper)
        else:
            raise ValueError(f"Unknown token: {tok}")
    return processed

def _infix_to_postfix(tokens: List[str]) -> List[str]:
    precedence = {'NOT': 3, 'AND': 2, 'OR': 1, 'XOR': 1}
    output = []
    stack = []
    for tok in tokens:
        if tok in ('TRUE', 'FALSE'):
            output.append(tok)
        elif tok == '(':
            stack.append(tok)
        elif tok == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            if not stack:
                raise ValueError("Mismatched parentheses")
            stack.pop()
        elif tok in precedence:
            while (stack and stack[-1] != '(' and
                   precedence.get(stack[-1], 0) >= precedence[tok]):
                output.append(stack.pop())
            stack.append(tok)
        else:
            raise ValueError(f"Unknown token in expression: {tok}")
    while stack:
        op = stack.pop()
        if op == '(':
            raise ValueError("Mismatched parentheses")
        output.append(op)
    return output

def _evaluate_postfix(postfix: List[str]) -> bool:
    stack = []
    for tok in postfix:
        if tok == 'TRUE':
            stack.append(True)
        elif tok == 'FALSE':
            stack.append(False)
        elif tok == 'NOT':
            if len(stack) < 1:
                raise ValueError("Insufficient operands for NOT")
            val = stack.pop()
            stack.append(not val)
        elif tok in ('AND', 'OR', 'XOR'):
            if len(stack) < 2:
                raise ValueError(f"Insufficient operands for {tok}")
            right = stack.pop()
            left = stack.pop()
            if tok == 'AND':
                stack.append(left and right)
            elif tok == 'OR':
                stack.append(left or right)
            elif tok == 'XOR':
                stack.append(left != right)
        else:
            raise ValueError(f"Unknown token: {tok}")
    if len(stack) != 1:
        raise ValueError("Invalid expression")
    return stack[0]

if __name__ == '__main__':
    test_cases = [
        ("True AND False", False),
        ("True OR False", True),
        ("NOT True", False),
        ("True XOR True", False),
        ("(True OR False) AND True", True),
        ("NOT (True AND False)", True),
        ("True AND (False OR True)", True),
    ]
    for expr, expected in test_cases:
        result = analyze_boolean_expression(expr)
        status = "PASS" if result == expected else "FAIL"