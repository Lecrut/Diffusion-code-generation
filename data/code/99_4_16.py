def parse_and_compute(expression):
    def helper(s):
        if s.isdigit():
            return int(s)
        stack = []
        num = 0
        op = '+'
        i = 0
        while i < len(s):
            if s[i] == '(':
                j = s.find(')', i)
                num = helper(s[i+1:j])
                i = j + 1
            elif s[i].isdigit():
                num = num * 10 + int(s[i])
                i += 1
            else:
                if op == '+':
                    stack.append(num)
                elif op == '-':
                    stack.append(-num)
                elif op == '*':
                    stack.append(stack.pop() * num)
                elif op == '/':
                    stack.append(int(stack.pop() / num))
                op = s[i]
                num = 0
                i += 1
        if op == '+':
            stack.append(num)
        elif op == '-':
            stack.append(-num)
        elif op == '*':
            stack.append(stack.pop() * num)
        elif op == '/':
            stack.append(int(stack.pop() / num))
        return sum(stack)

    return helper(expression)

if __name__ == '__main__':
    print(parse_and_compute("(1 + 2) * (3 - 4)"))