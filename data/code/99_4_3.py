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
                num, sub_num = helper(s[s.find('(') + 1:s.rfind(')')])
                if op == '+':
                    stack.append(sub_num)
                elif op == '-':
                    stack.append(-sub_num)
                elif op == '*':
                    stack[-1] *= sub_num
                elif op == '/':
                    stack[-1] = int(stack[-1] / sub_num)
                num = 0
                op = char
            else:
                if op == '+':
                    stack.append(num)
                elif op == '-':
                    stack.append(-num)
                elif op == '*':
                    stack[-1] *= num
                elif op == '/':
                    stack[-1] = int(stack[-1] / num)
                num = 0
                op = char
        if op == '+':
            stack.append(num)
        elif op == '-':
            stack.append(-num)
        elif op == '*':
            stack[-1] *= num
        elif op == '/':
            stack[-1] = int(stack[-1] / num)
        return (sum(stack), s.find(')') + 1 if ')' in s else len(s))
    return helper(expression)[0]
if __name__ == '__main__':
    print(parse_and_compute('(2+3)*(4-5)'))