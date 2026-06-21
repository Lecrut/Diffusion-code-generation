class TwoSumFinder:
    HASH_TABLE_SIZE = 1024

    @staticmethod
    def _hash(num):
        return num % TwoSumFinder.HASH_TABLE_SIZE

    def __init__(self):
        self.hash_table = [None] * TwoSumFinder.HASH_TABLE_SIZE

    def find_pair_sum(self, nums, target):
        for index, num in enumerate(nums):
            complement = target - num
            complement_hash = TwoSumFinder._hash(complement)
            if self.hash_table[complement_hash] is not None:
                return [self.hash_table[complement_hash], index]
            num_hash = TwoSumFinder._hash(num)
            self.hash_table[num_hash] = index
        raise ValueError("No two sum solution")

if __name__ == '__main__':
    finder = TwoSumFinder()
    nums = [4, 9, 11, 3, 7]
    target = 10
    result = finder.find_pair_sum(nums, target)
    print(result)