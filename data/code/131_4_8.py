def is_balanced(expression):
    stack = []
    brackets = {'(': ')', '[': ']', '{': '}'}
    
    for char in expression:
        if char in brackets.keys():
            stack.append(char)
        elif char in brackets.values():
            if not stack or brackets[stack.pop()] != char:
                return False
    
    return len(stack) == 0

if __name__ == '__main__':
    sample_expression = "(([]{}))(()())"
    result = is_balanced(sample_expression)
    print(result)