class BooleanLogic:
    def evaluate_expression(self, a, b, c):
        a_and_b = a & b
        not_c = 1 - c
        result = a_and_b | not_c
        return result
if __name__ == '__main__':
    logic = BooleanLogic()
    a_val = 1
    b_val = 0
    c_val = 1
    result = logic.evaluate_expression(a_val, b_val, c_val)
    print(result)