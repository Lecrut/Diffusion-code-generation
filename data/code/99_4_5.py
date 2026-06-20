def parse_and_compute(expression):
    def helper(s, start, end):
        if start == end:
            return int(s[start])
        num = 0
        op = '+'
        i = start
        while i < end:
            char = s[i]
            if char.isdigit():
                num = num * 10 + int(char)
            elif char in '+-*/':
                if op == '+':
                    stack.append(num)
                elif op == '-':
                    stack.append(-num)
                elif op == '*':
                    stack.append(stack.pop() * num)
                elif op == '/':
                    stack.append(int(stack.pop() / num))
                num = 0
                op = char
            i += 1
        if op in '+-':
            stack.append(num if op == '+' else -num)
        elif op in '*/':
            stack.append(int(stack.pop() * num) if op == '*' else int(stack.pop() / num))
        return sum(stack)

    stack = []
    return helper(expression, 0, len(expression))

if __name__ == '__main__':
    print(parse_and_compute('1 + (2 * (3 + 4))'))
    print(parse_and_compute('(5 - 6) * 7'))