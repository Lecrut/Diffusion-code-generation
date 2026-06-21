class BooleanExpressionEvaluator:
    def __init__(self, left_operand_a, left_operand_b, right_operand_c, right_operand_d):
        self.left_first = bool(left_operand_a)
        self.left_second = bool(left_operand_b)
        self.right_first = bool(right_operand_c)
        self.right_second = bool(right_operand_d)

    def compute(self):
        left_part = self.left_first and self.left_second
        right_part = self.right_first and (not self.right_second)
        final_result = left_part or right_part
        return final_result

if __name__ == '__main__':
    evaluator = BooleanExpressionEvaluator(0, 1, 0, 0)
    answer = evaluator.compute()
    print(answer)