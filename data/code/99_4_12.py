def parse_and_compute(expression):
    def helper(s):
        if s.isdigit():
            return int(s)
        else:
            op = None
            num = 0
            stack = []
            for char in s:
                if char == '(':
                    stack.append(num)
                    num = 0
                elif char.isdigit():
                    num = num * 10 + int(char)
                elif char in '+-*/':
                    if op is not None:
                        left = stack.pop()
                        if op == '+':
                            stack.append(left + num)
                        elif op == '-':
                            stack.append(left - num)
                        elif op == '*':
                            stack.append(left * num)
                        elif op == '/':
                            stack.append(int(left / num))
                    else:
                        stack.append(num)
                    op = char
                    num = 0
                elif char == ')':
                    left = stack.pop()
                    if op == '+':
                        stack.append(left + num)
                    elif op == '-':
                        stack.append(left - num)
                    elif op == '*':
                        stack.append(left * num)
                    elif op == '/':
                        stack.append(int(left / num))
                    return helper(''.join(map(str, stack)))
            return num
    return helper(expression)

if __name__ == '__main__':
    print(parse_and_compute("(1 + 2) * (3 - 4)"))