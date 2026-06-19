class AdjacentElementChecker:
    def __init__(self, elements):
        self.elements = elements

    def is_non_decreasing(self):
        return all(x <= y for x, y in zip(self.elements, self.elements[1:]))

if __name__ == '__main__':
    sample_input_1 = [1, 3, 5, 7, 9]
    checker_1 = AdjacentElementChecker(sample_input_1)
    print(checker_1.is_non_decreasing())

    sample_input_2 = [1, 5, 3, 7]
    checker_2 = AdjacentElementChecker(sample_input_2)
    print(checker_2.is_non_decreasing())

    sample_input_3 = [10, 20, 20, 30]
    checker_3 = AdjacentElementChecker(sample_input_3)
    print(checker_3.is_non_decreasing())

    sample_input_4 = [5, 5, 5]
    checker_4 = AdjacentElementChecker(sample_input_4)
    print(checker_4.is_non_decreasing())

    sample_input_5 = [1, 2, 1]
    checker_5 = AdjacentElementChecker(sample_input_5)
    print(checker_5.is_non_decreasing())