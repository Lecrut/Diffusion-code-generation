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
                num, sub_num = helper(s[s.find('(')+1:s.rfind(')')])
                if op == '+':
                    stack.append(sub_num)
                elif op == '-':
                    stack.append(-sub_num)
                elif op == '*':
                    stack[-1] *= sub_num
                elif op == '/':
                    stack[-1] //= sub_num
                num = 0
            elif char in '+-*/':
                if op == '+':
                    stack.append(num)
                elif op == '-':
                    stack.append(-num)
                elif op == '*':
                    stack[-1] *= num
                elif op == '/':
                    stack[-1] //= num
                op = char
                num = 0
        if op == '+':
            stack.append(num)
        elif op == '-':
            stack.append(-num)
        elif op == '*':
            stack[-1] *= num
        elif op == '/':
            stack[-1] //= num
        return sum(stack), s.find(')') + 1

    return helper(expression)[0]

if __name__ == '__main__':
    print(parse_and_compute("2*(3+4)"))
    print(parse_and_compute("(5-2)*(3+7)"))