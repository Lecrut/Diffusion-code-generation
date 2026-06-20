def is_balanced_parentheses(expression):
    stack = []
    matching_brackets = {')': '(', '}': '{', ']': '['}
    for char in expression:
        if char in matching_brackets.values():
            stack.append(char)
        elif char in matching_brackets.keys():
            if not stack or stack.pop() != matching_brackets[char]:
                return False
        else:
            continue
    return len(stack) == 0
if __name__ == '__main__':
    sample_expression = '((2 * (3 + 4)) / [5 - {6 / (7 + 8)}])'
    result = is_balanced_parentheses(sample_expression)
    print(result)