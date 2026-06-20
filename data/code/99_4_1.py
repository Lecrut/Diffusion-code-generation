def parse_and_compute(expression):
    def helper(s):
        if s.isdigit():
            return int(s)
        stack = []
        num = 0
        op = '+'
        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)
            elif char == '(':
                num, sub_result = helper(s[s.find('(')+1:s.rfind(')')])
                if op == '+':
                    stack.append(sub_result)
                elif op == '-':
                    stack.append(-sub_result)
                elif op == '*':
                    stack[-1] *= sub_result
                elif op == '/':
                    stack[-1] = int(stack[-1] / sub_result)
                num = 0
            elif char in '+-*/':
                if op == '+':
                    stack.append(num)
                elif op == '-':
                    stack.append(-num)
                elif op == '*':
                    stack[-1] *= num
                elif op == '/':
                    stack[-1] = int(stack[-1] / num)
                op = char
                num = 0
        if op == '+':
            stack.append(num)
        elif op == '-':
            stack.append(-num)
        elif op == '*':
            stack[-1] *= num
        elif op == '/':
            stack[-1] = int(stack[-1] / num)
        return sum(stack)

    return helper(expression.strip())

if __name__ == '__main__':
    print(parse_and_compute("3+(2*5)"))
    print(parse_and_compute("(1+2)*3"))
    print(parse_and_compute("4*(2+(3-1))"))