def adjacent_pair_generator(lst):
    for i in range(len(lst) - 1):
        yield lst[i] > lst[i + 1]

class AdjacentPairChecker:
    def __init__(self, lst):
        self.lst = lst

    def check_pairs(self):
        return list(adjacent_pair_generator(self.lst))

if __name__ == '__main__':
    sample_input_1 = [1, 3, 5, 7, 9]
    checker_1 = AdjacentPairChecker(sample_input_1)
    result_1 = checker_1.check_pairs()
    print(result_1)

    sample_input_2 = [1, 3, 2, 5]
    checker_2 = AdjacentPairChecker(sample_input_2)
    result_2 = checker_2.check_pairs()
    print(result_2)

    sample_input_3 = [10, 20, 20, 30]
    checker_3 = AdjacentPairChecker(sample_input_3)
    result_3 = checker_3.check_pairs()
    print(result_3)

    sample_input_4 = [5, 5, 5]
    checker_4 = AdjacentPairChecker(sample_input_4)
    result_4 = checker_4.check_pairs()
    print(result_4)

    sample_input_5 = [1, 2, 1]
    checker_5 = AdjacentPairChecker(sample_input_5)
    result_5 = checker_5.check_pairs()
    print(result_5)