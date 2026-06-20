PARENTHESIS_PAIRS = {
    '(': ')',
    '[': ']',
    '{': '}'
}

def is_balanced(expression):
    stack = []
    for char in expression:
        if char in PARENTHESIS_PAIRS:
            stack.append(char)
        elif char in PARENTHESIS_PAIRS.values():
            if not stack or PARENTHESIS_PAIRS[stack.pop()] != char:
                return False
    return not stack

if __name__ == '__main__':
    test_expression = "((2 + 3) * [4 - 5])"
    result = is_balanced(test_expression)
    print(result)