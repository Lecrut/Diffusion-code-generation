def parse_and_compute(expression):

    def helper(s):
        if s.isdigit():
            return int(s)
        stack = []
        num = 0
        sign = '+'
        for i, char in enumerate(s):
            if char.isdigit():
                num = num * 10 + int(char)
            if not char.isdigit() and char != ' ' or i == len(s) - 1:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                elif sign == '/':
                    stack.append(int(stack.pop() / num))
                sign = char
                num = 0
        return sum(stack)

    def parse(s):
        if s[0] != '(' or s[-1] != ')':
            raise ValueError('Invalid expression')
        s = s[1:-1]
        balance = 0
        for i, char in enumerate(s):
            if char == '(':
                balance += 1
            elif char == ')':
                balance -= 1
            if balance == 0 and (i == len(s) - 1 or not s[i + 1].isdigit()):
                return (helper(s[:i + 1]), i + 2)
        raise ValueError('Unbalanced parentheses')

    def recursive_parse(expression):
        while '(' in expression:
            value, start = parse(expression)
            expression = expression[:start - 1] + str(value) + expression[start:]
        return helper(expression)
    return recursive_parse(expression)
if __name__ == '__main__':
    print(parse_and_compute('(3+5)*2'))
    print(parse_and_compute('((10/2)+3)*4'))