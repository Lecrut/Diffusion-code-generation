class ListComprehensionChecker:
    def __init__(self):
        self.sample_start = 0
        self.sample_end = 10

    def generate_list_comprehension(self, start, end, operation):
        return [operation(x) for x in range(start, end)]

    def compare_comprehensions(self, list_comp1, list_comp2):
        return set(list_comp1) == set(list_comp2)

if __name__ == '__main__':
    checker = ListComprehensionChecker()
    sample_operation = lambda x: x**3
    list_comp1 = checker.generate_list_comprehension(checker.sample_start, checker.sample_end, sample_operation)
    list_comp2 = checker.generate_list_comprehension(checker.sample_start, checker.sample_end, sample_operation)
    result = checker.compare_comprehensions(list_comp1, list_comp2)
    print(result)