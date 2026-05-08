class BooleanLogic:
    def evaluate_expression(self, a, b, c):
        result = (a & b) | (~c)
        return result
if __name__ == '__main__':
    logic = BooleanLogic()
    a_val = 1
    b_val = 0
    c_val = 1
    result = logic.evaluate_expression(a_val, b_val, c_val)
    print(result)