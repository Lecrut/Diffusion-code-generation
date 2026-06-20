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
                num, sub_result = helper(s[s.index(char) + 1:])
                if op == '+':
                    stack.append(num)
                elif op == '-':
                    stack.append(-num)
                elif op == '*':
                    stack[-1] *= num
                elif op == '/':
                    stack[-1] //= num
                num, op = sub_result
            elif char in '+-*/':
                if op == '+':
                    stack.append(num)
                elif op == '-':
                    stack.append(-num)
                elif op == '*':
                    stack[-1] *= num
                elif op == '/':
                    stack[-1] //= num
                num, op = 0, char
        return sum(stack), op

    return helper(expression)[0]

if __name__ == '__main__':
    print(parse_and_compute("2*(3+4)"))
    print(parse_and_compute("(5-2)*(3+7)"))