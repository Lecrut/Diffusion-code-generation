def evaluate_boolean_expression(expression: str) -> bool:
    tokens = []
    i = 0
    length = len(expression)
    while i < length:
        char = expression[i]
        if char == ' ':
            i += 1
            continue
        if char == '(':
            tokens.append('(')
            i += 1
        elif char == ')':
            tokens.append(')')
            i += 1
        elif char.isalpha():
            word = []
            while i < length and expression[i].isalpha():
                word.append(expression[i])
                i += 1
            word_str = ''.join(word)
            if word_str == 'AND':
                tokens.append('and')
            elif word_str == 'OR':
                tokens.append('or')
            elif word_str == 'NOT':
                tokens.append('not')
            elif word_str == 'True':
                tokens.append(True)
            elif word_str == 'False':
                tokens.append(False)
            else:
                raise ValueError(f"Unknown token: {word_str}")
        else:
            raise ValueError(f"Unexpected character: {char}")
    
    precedence = {'and': 2, 'or': 1}
    output_queue = []
    operator_stack = []
    
    for token in tokens:
        if isinstance(token, bool):
            output_queue.append(token)
        elif token == '(':
            operator_stack.append(token)
        elif token == ')':
            while operator_stack and operator_stack[-1] != '(':
                output_queue.append(operator_stack.pop())
            if not operator_stack:
                raise ValueError("Mismatched parentheses")
            operator_stack.pop()
        elif token in ('and', 'or', 'not'):
            while (operator_stack and 
                   operator_stack[-1] != '(' and
                   ((token in ('and', 'or') and precedence.get(operator_stack[-1], 0) >= precedence.get(token, 0)) or
                    (token == 'not' and operator_stack[-1] == 'not'))):
                output_queue.append(operator_stack.pop())
            operator_stack.append(token)
            
    while operator_stack:
        if operator_stack[-1] == '(':
            raise ValueError("Mismatched parentheses")
        output_queue.append(operator_stack.pop())
        
    eval_stack = []
    for token in output_queue:
        if isinstance(token, bool):
            eval_stack.append(token)
        elif token == 'not':
            if len(eval_stack) < 1:
                raise ValueError("Insufficient operands for NOT")
            val = eval_stack.pop()
            eval_stack.append(not val)
        elif token == 'and':
            if len(eval_stack) < 2:
                raise ValueError("Insufficient operands for AND")
            b = eval_stack.pop()
            a = eval_stack.pop()
            eval_stack.append(a and b)
        elif token == 'or':
            if len(eval_stack) < 2:
                raise ValueError("Insufficient operands for OR")
            b = eval_stack.pop()
            a = eval_stack.pop()
            eval_stack.append(a or b)
            
    if len(eval_stack) != 1:
        raise ValueError("Invalid expression")
        
    return eval_stack[0]

if __name__ == '__main__':
    expr = "True AND (False OR NOT False)"
    result = evaluate_boolean_expression(expr)
    print(result)