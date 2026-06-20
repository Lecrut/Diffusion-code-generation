def is_balanced_parentheses(expression):
    stack = []
    parentheses_map = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in "([{":
            stack.append(char)
        elif char in ")]}":
            if not stack or parentheses_map[char] != stack.pop():
                return False

    return len(stack) == 0

if __name__ == '__main__':
    sample_expression = "{[(())]}[()]{}"
    result = is_balanced_parentheses(sample_expression)
    print(result)