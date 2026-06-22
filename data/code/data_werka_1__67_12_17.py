class MaxProductFinder:
    def __init__(self, nums):
        self.nums = nums

    def find_max_product_pair(self):
        if len(self.nums) < 2:
            raise ValueError('List must contain at least two elements')
        
        max1 = max2 = float('-inf')
        min1 = min2 = float('inf')
        
        for num in self.nums:
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
    finder = MaxProductFinder([1, 10, -5, 1, -100])
    result = finder.find_max_product_pair()
    print(result)
    
    finder2 = MaxProductFinder([-10, -20, 5, 6])
    result2 = finder2.find_max_product_pair()
    print(result2)