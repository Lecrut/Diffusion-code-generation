def evaluate_expression(expr: str) -> bool:
    allowed = {"and", "or", "not", "=", "!=", "<", ">"}
    def is_allowed(token):
        return token in allowed or (isinstance(token, int))
    tokens = expr.split()
    if not all(is_allowed(t) for t in tokens):
        raise ValueError("Invalid expression")
    stack = []
    i = 0
    while i < len(tokens):
        op1 = None
        current_token = tokens[i]
        if current_token == "not":
            op2, val = evaluate_unary(current_token)
            stack.append(val)
            continue
        try:
            num_val = int(current_token)
            stack.append(num_val != 0) 
        except ValueError:
            pass
    return all(stack)
def evaluate_unary(op):
    if op == "not":
        raise NotImplementedError("Complex recursion not supported in this static version")
    return None
if __name__ == '__main__':
    expr = "(a and b) or c"
    mapping = {"a": True, "b": False, "c": True}
    try:
        result = eval(expr, {"__builtins__": {}, **mapping}, {})
        print(result)
    except Exception as e:
        print(f"Error: {e}")