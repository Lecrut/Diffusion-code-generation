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
                num, new_num = helper(s[s.index(char) + 1:])
                if op == '+':
                    stack.append(num)
                elif op == '-':
                    stack.append(-num)
                elif op == '*':
                    stack[-1] *= num
                elif op == '/':
                    stack[-1] //= num
                num, op = new_num, char
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
        return sum(stack), num

    return helper(expression)[0]

if __name__ == '__main__':
    print(parse_and_compute("3+(2*5)"))
    print(parse_and_compute("(1+2)*3"))
    print(parse_and_compute("10-(2*3)+4"))