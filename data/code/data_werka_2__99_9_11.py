class BooleanConditionEvaluator:
    def __init__(self, val_a, val_b, val_c):
        self.val_a = val_a
        self.val_b = val_b
        self.val_c = val_c

    def evaluate_with_operator_module(self):
        import operator
        step1 = operator.and_(self.val_a, self.val_b)
        step2 = operator.or_(step1, self.val_c)
        return step2

    def evaluate_with_keywords_precedence(self):
        return self.val_a and self.val_b or self.val_c

    def evaluate_with_explicit_parentheses(self):
        return (self.val_a and self.val_b) or self.val_c

    def evaluate_with_different_grouping(self):
        return self.val_a and (self.val_b or self.val_c)

    def get_results(self):
        res_op = self.evaluate_with_operator_module()
        res_kw = self.evaluate_with_keywords_precedence()
        res_exp = self.evaluate_with_explicit_parentheses()
        res_grp = self.evaluate_with_different_grouping()
        return {
            "operator_module_result": res_op,
            "keyword_precedence_result": res_kw,
            "explicit_parentheses_result": res_exp,
            "different_grouping_result": res_grp
        }

if __name__ == '__main__':
    evaluator = BooleanConditionEvaluator(True, False, True)
    results = evaluator.get_results()
    print(results)
    print(evaluator.evaluate_with_different_grouping())