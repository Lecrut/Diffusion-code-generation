class ListComprehensionComparator:
    @staticmethod
    def generate_list_comprehension(start, end, operation):
        return [operation(x) for x in range(start, end)]

    @staticmethod
    def compare_comprehensions(list_comp1, list_comp2):
        return set(list_comp1) == set(list_comp2)

if __name__ == '__main__':
    sample_start = 0
    sample_end = 10
    operation = lambda x: x**2

    list_comp1 = ListComprehensionComparator.generate_list_comprehension(sample_start, sample_end, operation)
    list_comp2 = ListComprehensionComparator.generate_list_comprehension(sample_start, sample_end, operation)

    result = ListComprehensionComparator.compare_comprehensions(list_comp1, list_comp2)
    print(result)