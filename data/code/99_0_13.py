import operator

def evaluate_expression(expression):
    ops = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
    stack = []
    current_number = 0
    current_operator = '+'

    for char in expression:
        if char.isdigit():
            current_number = current_number * 10 + int(char)
        elif char in ops:
            if current_operator == '+':
                stack.append(current_number)
            elif current_operator == '-':
                stack.append(-current_number)
            elif current_operator == '*':
                stack.append(stack.pop() * current_number)
            elif current_operator == '/':
                stack.append(int(stack.pop() / current_number))
            current_operator = char
            current_number = 0

    if current_operator == '+':
        stack.append(current_number)
    elif current_operator == '-':
        stack.append(-current_number)

    return sum(stack)

if __name__ == '__main__':
    print(evaluate_expression("3+5*2-8/4"))