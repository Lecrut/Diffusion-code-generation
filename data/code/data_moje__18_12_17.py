def median_index(lst):
    if not lst:
        raise ValueError("List must not be empty")
    
    n = len(lst)
    if n % 2 == 1:
        return lst[n // 2]
    
    even_idx = n // 2
    low = 0
    high = n - 1
    pos = low + (even_idx - low) // 2
    
    while True:
        pivot = lst[pos]
        lt = 0
        eq = 0
        gt = 0
        
        for val in lst:
            if val < pivot:
                lt += 1
            elif val == pivot:
                eq += 1
            else:
                gt += 1
        
        if lt < even_idx and lt + eq > even_idx:
            return pivot
        
        if lt + eq <= even_idx:
            target = even_idx - (lt + eq)
            high = pos + eq
            pos = low + (high - low) // 2
        else:
            low = lt + eq
            pos = low + (high - low) // 2

if __name__ == '__main__':
    sample_list = [12, 4, 5, 6, 7, 3, 1, 9, 8, 2]
    result = median_index(sample_list)
    print(result)