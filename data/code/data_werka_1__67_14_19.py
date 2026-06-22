class PairFinder:
    def __init__(self, nums):
        self.nums = nums

    def find_pair_with_sum(self, target):
        num_set = set()
        for num in self.nums:
            complement = target - num
            if complement in num_set:
                return (complement, num)
            num_set.add(num)
        raise ValueError("No two distinct elements add up to the target value")

if __name__ == '__main__':
    sample_list = [3, 6, 8, 12]
    target_value = 14
    pair_finder = PairFinder(sample_list)
    try:
        result = pair_finder.find_pair_with_sum(target_value)
        print(result)
    except ValueError as e:
        print(e)

    another_target = 20
    try:
        result = pair_finder.find_pair_with_sum(another_target)
        print(result)
    except ValueError as e:
        print(e)