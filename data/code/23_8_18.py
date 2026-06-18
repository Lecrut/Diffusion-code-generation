def __init__(self):
        pass

if __name__ == '__main__':
    comp = VectorComparator()
    
    # Sample Test Cases
    
    # Case 1: [1, 2], [1, 4] -> Diff at index 1 (2 vs 4). 2 <= 4 True. Return True.
    v1 = [1, 2]
    v2 = [1, 4]
    
    # Case 2: [5, 3], [4, 6] -> Diff at index 0 (5 vs 4). 5 <= 4 False. Return False. Stop early.
    v3 = [5, 3]
    v4 = [4, 6]
    
    # Case 3: Identical vectors. No diff found. Based on logic above -> False. 
    # (If the intent was to treat equal as True, this would return True. But "first differing" implies a difference is required).
    v5 = [10]
    v6 = [10]

    print("Case 1:", comp.element_wise_less_equal(v1, v2)) # Expected: True
    print("Case 2:", comp.element_wise_less_equal(v3, v4)) # Expected: False
    print("Case 3 (Equal):", comp.element_wise_less_equal(v5, v6)) # Expected: False based on "first differing" logic
    
    # Case 4: Different lengths. [1], [2]. Diff at index