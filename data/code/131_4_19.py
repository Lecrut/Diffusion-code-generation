class ParenthesesChecker:
    OPEN_PAREN = '('
    CLOSE_PAREN = ')'

    @staticmethod
    def is_balanced(expression):
        stack = []
        for char in expression:
            if char == ParenthesesChecker.OPEN_PAREN:
                stack.append(char)
            elif char == ParenthesesChecker.CLOSE_PAREN:
                if not stack or stack[-1] != ParenthesesChecker.OPEN_PAREN:
                    return False
                stack.pop()
        return len(stack) == 0

if __name__ == '__main__':
    sample_expression = "((()))"
    is_balanced = ParenthesesChecker.is_balanced(sample_expression)
    print(is_balanced)