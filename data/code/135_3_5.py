def are_equivalent(expr1, expr2):
    def evaluate(expr):
        return eval(expr)
    try:
        val1 = evaluate(expr1)
        val2 = evaluate(expr2)
        return val1 == val2
    except Exception:
        return False
if __name__ == '__main__':
    print(are_equivalent("True", "True"))
    print(are_equivalent("True", "False"))
    print(are_equivalent("1", "True"))
    print(are_equivalent("(A or B)", "(A or B)"))
    print(are_equivalent("A and B", "B and A"))
    print(are_equivalent("True", "1"))
    print(are_equivalent("False", "0"))
    print(are_equivalent("(A or B)", "(B or A)"))