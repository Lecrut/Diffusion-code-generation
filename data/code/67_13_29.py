class PairFinder:
    @staticmethod
    def find_pair_with_sum(nums, target):
        num_set = set()
        for num in nums:
            complement = target - num
            if complement in num_set:
                return (complement, num)
            num_set.add(num)
        raise ValueError("No pair found that adds up to the target sum.")

if __name__ == '__main__':
    sample_list = [10, 15, 3, 7]
    target_sum = 17
    try:
        result = PairFinder.find_pair_with_sum(sample_list, target_sum)
        print(result)
    except ValueError as e:
        print(e)