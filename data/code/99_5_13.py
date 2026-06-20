def calculate_expression(operands, operators):
    for op in ('*', '/'):
        while op in operators:
            index = operators.index(op)
            if op == '*':
                operands[index] *= operands.pop(index + 1)
            else:
                operands[index] /= operands.pop(index + 1)
            del operators[index]
    return sum(operands)

if __name__ == '__main__':
    print(calculate_expression([2, 3, 4, 5], ['+', '*', '-']))