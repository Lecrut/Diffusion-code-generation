def is_balanced(expression):
    STACK_OPEN = "({["
    STACK_CLOSE = ")}]"
    
    stack = []
    for char in expression:
        if char in STACK_OPEN:
            stack.append(char)
        elif char in STACK_CLOSE:
            if not stack or stack.pop() != STACK_CLOSE[STACK_OPEN.index(char)]:
                return False
    return not stack

if __name__ == '__main__':
    sample_expression = "({[]})"
    print(is_balanced(sample_expression))