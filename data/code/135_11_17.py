def is_logically_equivalent(p, q):
    from itertools import product

    def evaluate(expression, truth_values):
        stack = []
        for char in expression:
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
            elif char == '>':
                b, a = (stack.pop(), stack.pop())
                stack.append(not a or b)
        return stack[0]
    variables = set(p).union(set(q))
    truth_values = list(product([True, False], repeat=len(variables)))
    for tv in truth_values:
        p_val = evaluate(p, {v: t for v, t in zip(variables, tv)})
        q_val = evaluate(q, {v: t for v, t in zip(variables, tv)})
        if p_val != q_val:
            return False
    return True
if __name__ == '__main__':
    print(is_logically_equivalent('T', 'F'))
    print(is_logically_equivalent('T & T', 'F | F'))
    print(is_logically_equivalent('T & T', 'T & T'))
    print(is_logically_equivalent('(T > F) & (F > T)', 'T'))