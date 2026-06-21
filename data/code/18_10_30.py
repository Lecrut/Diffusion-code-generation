class ListEvaluator:
    def __init__(self, lst):
        self.lst = lst

    def is_first_greater_than_second(self):
        return self.lst[0] > self.lst[1]

if __name__ == '__main__':
    SAMPLE_LIST_1 = [15, 10]
    SAMPLE_LIST_2 = [2, 3]
    SAMPLE_LIST_3 = [7.8, 7.8]

    evaluator1 = ListEvaluator(SAMPLE_LIST_1)
    evaluator2 = ListEvaluator(SAMPLE_LIST_2)
    evaluator3 = ListEvaluator(SAMPLE_LIST_3)

    print(f"Is the first element of {SAMPLE_LIST_1} greater than the second? {evaluator1.is_first_greater_than_second()}")
    print(f"Is the first element of {SAMPLE_LIST_2} greater than the second? {evaluator2.is_first_greater_than_second()}")
    print(f"Is the first element of {SAMPLE_LIST_3} greater than the second? {evaluator3.is_first_greater_than_second()}")