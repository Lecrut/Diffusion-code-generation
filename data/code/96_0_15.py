def evaluate_nested_logic(a, b, c, d):

    def is_boolean(value):
        return isinstance(value, bool)
    if not all((is_boolean(x) for x in [a, b, c, d])):
        raise ValueError('All arguments must be boolean')
    return a and b or (c and (not d))
if __name__ == '__main__':
    A = True
    B = False
    C = True
    D = False
    result = evaluate_nested_logic(A, B, C, D)
    print(result)