def parse_and_compute(expression):
    def helper(s):
        if s.isdigit():
            return int(s)
        stack = []
        num = 0
        op = '+'
        for char in s:
            if char == '(':
                num, sub_result = helper(s[1:])
                if op == '+':
                    stack.append(num)
                elif op == '-':
                    stack.append(-num)
                elif op == '*':
                    stack[-1] *= num
                elif op == '/':
                    stack[-1] //= num
                num = 0
                op = char
            elif char.isdigit():
                num = num * 10 + int(char)
            elif char in '+-*/)':
                if op == '+':
                    stack.append(num)
                elif op == '-':
                    stack.append(-num)
                elif op == '*':
                    stack[-1] *= num
                elif op == '/':
                    stack[-1] //= num
                num = 0
                op = char
        return sum(stack), s[len(s) - len(sub_result):]

    result, _ = helper(expression[1:-1])
    return result

if __name__ == '__main__':
    print(parse_and_compute('(2 + (3 * 4))'))
    print(parse_and_compute('((10 / 2) - 5)'))