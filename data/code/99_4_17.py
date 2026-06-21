def evaluate_expression(expression: str):
    if not expression or not expression.strip():
        raise ValueError("Empty expression")
    
    expression = expression.strip()
    
    if expression.startswith("(") and expression.endswith(")"):
        balanced_count = 0
        split_index = -1
        for i, char in enumerate(expression):
            if char == '(':
                balanced_count += 1
            elif char == ')':
                balanced_count -= 1
            
            if balanced_count == 0 and i < len(expression) - 1:
                next_char = expression[i + 1]
                if next_char in ('+', '-'):
                    split_index = i + 1
                    break
                elif next_char in ('*', '/') and i + 2 < len(expression) and expression[i + 2] in ('+', '-'):
                    split_index = i + 1
                    break
        
        if split_index != -1:
            left_part = expression[1:split_index - 1]
            right_part = expression[split_index:]
            
            operator = right_part[0]
            right_operand_str = right_part[1:].strip()
            
            if not right_operand_str.startswith("(") or not right_operand_str.endswith(")"):
                try:
                    if '.' in right_operand_str:
                        right_operand = float(right_operand_str)
                    else:
                        right_operand = int(right_operand_str)
                except ValueError:
                    raise ValueError(f"Invalid operand: {right_operand_str}")
            else:
                right_operand = evaluate_expression(right_operand_str)
            
            left_operand = evaluate_expression(left_part)
            
            if operator == '+':
                return left_operand + right_operand
            elif operator == '-':
                return left_operand - right_operand
            elif operator == '*':
                return left_operand * right_operand
            elif operator == '/':
                if right_operand == 0:
                    raise ValueError("Division by zero")
                return left_operand / right_operand
            else:
                raise ValueError(f"Unsupported operator: {operator}")
        else:
            inner = expression[1:-1].strip()
            if not inner:
                raise ValueError("Empty parentheses")
            return evaluate_expression(inner)
    
    if not _is_valid_number(expression):
        raise ValueError(f"Invalid expression: {expression}")
    
    if '.' in expression:
        return float(expression)
    return int(expression)

def _is_valid_number(s: str) -> bool:
    if not s:
        return False
    try:
        float(s)
        return True
    except ValueError:
        return False

if __name__ == '__main__':
    print(evaluate_expression("((1 + 2) * (3 + 4))"))
    print(evaluate_expression("((10 / 2) + (3 * 4))"))
    print(evaluate_expression("(5)"))
    print(evaluate_expression("((1 + 1))"))
    print(evaluate_expression("((10 * (2 + 3)) / 5)"))