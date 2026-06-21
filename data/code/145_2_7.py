def evaluate_nested(flags):
    stack = []
    for flag in flags:
        if isinstance(flag, bool):
            stack.append(flag)
        elif flag == 'and':
            right = stack.pop()
            left = stack.pop()
            stack.append(left and right)
        elif flag == 'or':
            right = stack.pop()
            left = stack.pop()
            stack.append(left or right)
        elif flag == 'not':
            operand = stack.pop()
            stack.append(not operand)
    return stack[0]

if __name__ == '__main__':
    sample_flags = [True, False, 'not', 'and', True]
    print(evaluate_nested(sample_flags))