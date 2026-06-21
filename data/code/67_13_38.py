class PairFinder:
    def __init__(self, numbers):
        self.numbers = numbers

    def find_pair(self, target):
        num_set = set()
        for number in self.numbers:
            complement = target - number
            if complement in num_set:
                return (complement, number)
            num_set.add(number)
        raise ValueError("No pair found that adds up to the target sum.")

if __name__ == '__main__':
    sample_numbers = [10, 15, 3, 7]
    target_sum = 17
    pair_finder = PairFinder(sample_numbers)
    try:
        result = pair_finder.find_pair(target_sum)
        print(result)
    except ValueError as e:
        print(e)