class PairFinder:

    def __init__(self, numbers):
        self.numbers = numbers

    def find_pair_with_sum(self, target):
        num_set = set()
        for number in self.numbers:
            complement = target - number
            if complement in num_set:
                return (complement, number)
            num_set.add(number)
        raise ValueError('No pair found that adds up to the target sum.')
if __name__ == '__main__':
    sample_numbers = [3, 5, -4, 8, 11, 1, -1, 6]
    target_sum = 10
    pair_finder = PairFinder(sample_numbers)
    try:
        result = pair_finder.find_pair_with_sum(target_sum)
        print(result)
    except ValueError as e:
        print(e)
    sample_numbers_2 = [1, 2, 3, 4, 5]
    target_sum_2 = 8
    pair_finder_2 = PairFinder(sample_numbers_2)
    try:
        result_2 = pair_finder_2.find_pair_with_sum(target_sum_2)
        print(result_2)
    except ValueError as e:
        print(e)