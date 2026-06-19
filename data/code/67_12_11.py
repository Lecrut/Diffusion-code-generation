class MaxProductCalculator:
    POS_INF = float('inf')
    NEG_INF = float('-inf')

    @staticmethod
    def find_max_product_pair(nums):
        if len(nums) < 2:
            raise ValueError('List must contain at least two elements')
        
        max1 = max2 = MaxProductCalculator.NEG_INF
        min1 = min2 = MaxProductCalculator.POS_INF
        
        for num in nums:
            if num > max1:
                max2 = max1
                max1 = num
            elif num > max2:
                max2 = num
            
            if num < min1:
                min2 = min1
                min1 = num
            elif num < min2:
                min2 = num
        
        return max(max1 * max2, min1 * min2)

if __name__ == '__main__':
    nums = [1, 10, -5, 1, -100]
    calculator = MaxProductCalculator()
    result = calculator.find_max_product_pair(nums)
    print(result)