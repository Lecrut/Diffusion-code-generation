def evaluate_conditions(a, b, c, d, e):
    precedence_map = {
        'and': 2,
        'or': 1
    }
    op_stack = []
    val_stack = []

    def apply_operator():
        if not op_stack:
            return
        op = op_stack.pop()
        if len(val_stack) < 2:
            return
        right = val_stack.pop()
        left = val_stack.pop()
        if op == 'and':
            val_stack.append(left and right)
        elif op == 'or':
            val_stack.append(left or right)

    def get_precedence(op):
        return precedence_map.get(op, 0)

    def push_operator(op):
        while op_stack and get_precedence(op_stack[-1]) >= get_precedence(op):
            apply_operator()
        op_stack.append(op)

    val_stack.append(a)
    push_operator('and')
    val_stack.append(b)
    push_operator('or')
    val_stack.append(c)
    push_operator('and')
    val_stack.append(d)
    push_operator('or')
    val_stack.append(e)

    while op_stack:
        apply_operator()

    return val_stack[0] if val_stack else False

if __name__ == '__main__':
    res = evaluate_conditions(True, False, True, False, True)
    print(res)