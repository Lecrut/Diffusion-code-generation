def find_middle_value(nums):
    if not nums:
        raise ValueError("The list cannot be empty")
    
    def select_kth(k, arr):
        if len(arr) == 1:
            return arr[0]
        
        pivot = arr[len(arr) // 2]
        lows = [el for el in arr if el < pivot]
        highs = [el for el in arr if el > pivot]
        pivots = [el for el in arr if el == pivot]
        
        if k < len(lows):
            return select_kth(k, lows)
        elif k < len(lows) + len(pivots):
            return pivots[0]
        else:
            return select_kth(k - len(lows) - len(pivots), highs)
    
    mid_index = len(nums) // 2
    return select_kth(mid_index, nums)

if __name__ == '__main__':
    sample_values = [3, 1, 4, 1, 5, 9, 2]
    middle_value = find_middle_value(sample_values)
    print(middle_value)