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
            if (not char.isdigit() and char != ' ') or i == len(s) - 1:
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
            raise ValueError("Invalid expression")
        s = s[1:-1]
        balance = 0
        start = 0
        for i, char in enumerate(s):
            if char == '(':
                balance += 1
            elif char == ')':
                balance -= 1
            if balance == 0:
                return parse_and_compute(helper(s[start:i + 1])) + parse_and_compute(helper(s[i + 2:]))
        return helper(s)

    return parse(expression)

if __name__ == '__main__':
    print(parse_and_compute("(3+(4*5))"))