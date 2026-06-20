class ParenthesesChecker:
    def __init__(self):
        self.stack = []

    def is_balanced(self, expression):
        for char in expression:
            if char == '(':
                self.stack.append(char)
            elif char == ')':
                if not self.stack:
                    return False
                self.stack.pop()
        return len(self.stack) == 0

if __name__ == '__main__':
    checker = ParenthesesChecker()
    sample_expression = "((())(()))"
    balanced = checker.is_balanced(sample_expression)
    print(balanced)