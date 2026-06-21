def find_middle_value(nums):
    if not nums:
        raise ValueError("The list cannot be empty")
    
    def select_kth(arr, k):
        if len(arr) == 1:
            return arr[0]
        
        pivot = arr[len(arr) // 2]
        lows = [el for el in arr if el < pivot]
        highs = [el for el in arr if el > pivot]
        pivots = [el for el in arr if el == pivot]
        
        if k < len(lows):
            return select_kth(lows, k)
        elif k < len(lows) + len(pivots):
            return pivots[0]
        else:
            return select_kth(highs, k - len(lows) - len(pivots))
    
    mid_index = len(nums) // 2
    return select_kth(nums, mid_index)

if __name__ == '__main__':
    sample_values = [7, 10, 4, 3, 20, 15]
    middle_value = find_middle_value(sample_values)
    print(middle_value)