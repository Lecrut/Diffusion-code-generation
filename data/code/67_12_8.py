class MaxProductPair:
    MAX_PAIR = (float('-inf'), float('-inf'))
    MIN_PAIR = (float('inf'), float('inf'))

    @staticmethod
    def update_max_pair(pair, num):
        if num > pair[0]:
            return (num, pair[0])
        elif num > pair[1]:
            return (pair[0], num)
        return pair

    @staticmethod
    def update_min_pair(pair, num):
        if num < pair[0]:
            return (num, pair[0])
        elif num < pair[1]:
            return (pair[0], num)
        return pair

    @staticmethod
    def max_product(nums):
        if len(nums) < 2:
            raise ValueError('List must contain at least two elements')
        max_pair = MaxProductPair.MAX_PAIR
        min_pair = MaxProductPair.MIN_PAIR
        for num in nums:
            max_pair = MaxProductPair.update_max_pair(max_pair, num)
            min_pair = MaxProductPair.update_min_pair(min_pair, num)
        return max(max_pair[0] * max_pair[1], min_pair[0] * min_pair[1])
if __name__ == '__main__':
    nums = [1, 10, -5, 1, -100]
    result = MaxProductPair.max_product(nums)
    print(result)