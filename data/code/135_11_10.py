def evaluate_statement(statement, truth_values):
    stack = []
    for char in statement:
        if char == 'T':
            stack.append(True)
        elif char == 'F':
            stack.append(False)
        elif char == '!':
            stack[-1] = not stack[-1]
        elif char == '&':
            stack.append(stack.pop() and stack.pop())
        elif char == '|':
            stack.append(stack.pop() or stack.pop())
    return stack[0]

def are_equivalent(statement1, statement2):
    truth_values = ['TTT', 'TTF', 'TFT', 'TFF', 'FTT', 'FTF', 'FFT', 'FFF']
    for values in truth_values:
        if evaluate_statement(statement1, values) != evaluate_statement(statement2, values):
            return False
    return True

if __name__ == '__main__':
    print(are_equivalent('TT&T|F', 'T&TT|F'))
    print(are_equivalent('TT&T|F', 'T&TT|FF'))