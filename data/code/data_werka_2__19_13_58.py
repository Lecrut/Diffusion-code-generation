class TruthyEvaluator:
    def __init__(self, lst):
        self.lst = lst

    def has_truthy(self):
        return any(self.lst)

if __name__ == '__main__':
    sample_list1 = [0, False, None, '']
    sample_list2 = [0, False, None, 'hello']
    evaluator1 = TruthyEvaluator(sample_list1)
    evaluator2 = TruthyEvaluator(sample_list2)
    print(evaluator1.has_truthy())
    print(evaluator2.has_truthy())