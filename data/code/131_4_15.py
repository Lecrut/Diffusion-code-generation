class ParenthesesChecker:
    OPENING_BRACKETS = "([{"
    CLOSING_BRACKETS = ")]}"
    
    @staticmethod
    def is_balanced(expression):
        stack = []
        for char in expression:
            if char in ParenthesesChecker.OPENING_BRACKETS:
                stack.append(char)
            elif char in ParenthesesChecker.CLOSING_BRACKETS:
                if not stack or stack.pop() != ParenthesesChecker.OPENING_BRACKETS[ParenthesesChecker.CLOSING_BRACKETS.index(char)]:
                    return False
        return not stack

if __name__ == '__main__':
    sample_expression = "{[()]}"
    balanced = ParenthesesChecker.is_balanced(sample_expression)
    print(balanced)