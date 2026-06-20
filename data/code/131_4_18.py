def is_balanced_parentheses(expression):
    stack = []
    for char in expression:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack or stack[-1] != '(':
                return False
            stack.pop()
    return len(stack) == 0

if __name__ == '__main__':
    test_expression = "((a+b)*(c-d))"
    result = is_balanced_parentheses(test_expression)
    print(result)