def truth_table(expression):
    variables = set()
    for char in expression:
        if char.isalpha() and char.islower():
            variables.add(char)
    
    variable_count = len(variables)
    max_combinations = 2 ** variable_count
    
    def evaluate_expression(expr, assignment):
        stack = []
        i = 0
        while i < len(expr):
            if expr[i] == '1':
                stack.append(True)
            elif expr[i] == '0':
                stack.append(False)
            elif expr[i] in variables:
                index = list(variables).index(expr[i])
                stack.append(assignment[index])
            elif expr[i] == '!':
                stack[-1] = not stack[-1]
            elif expr[i] == '&':
                stack.append(stack.pop() and stack.pop())
            elif expr[i] == '|':
                stack.append(stack.pop() or stack.pop())
            i += 1
        return stack[0]
    
    for combination in range(max_combinations):
        assignment = [bool(combination & (1 << i)) for i in range(variable_count)]
        if evaluate_expression(expression, assignment) != evaluate_expression(expression, assignment[::-1]):
            return False
    return True

if __name__ == '__main__':
    expr1 = "a&b|!c"
    expr2 = "!c&a&b|!"
    print(truth_table(expr1) == truth_table(expr2))