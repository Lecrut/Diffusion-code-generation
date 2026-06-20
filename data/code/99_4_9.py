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
                num, sub_num = helper(s[s.index(char) + 1:])
                if op == '+':
                    stack.append(sub_num)
                elif op == '-':
                    stack.append(-sub_num)
                elif op == '*':
                    stack.append(stack.pop() * sub_num)
                elif op == '/':
                    stack.append(int(stack.pop() / sub_num))
                num = 0
            elif char in '+-*/':
                if op == '+':
                    stack.append(num)
                elif op == '-':
                    stack.append(-num)
                elif op == '*':
                    stack.append(stack.pop() * num)
                elif op == '/':
                    stack.append(int(stack.pop() / num))
                op = char
                num = 0
        if op == '+':
            stack.append(num)
        elif op == '-':
            stack.append(-num)
        elif op == '*':
            stack.append(stack.pop() * num)
        elif op == '/':
            stack.append(int(stack.pop() / num))
        return (sum(stack), s.index(')') + 1)
    result, _ = helper(expression[1:-1])
    return result
if __name__ == '__main__':
    print(parse_and_compute('(3+(2*4))'))
    print(parse_and_compute('((1+3)*5)'))