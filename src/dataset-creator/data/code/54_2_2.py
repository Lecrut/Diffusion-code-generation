def find_middle_index(sequence):
    if not sequence:
        return None
    n = len(sequence)
    if n % 2 == 0:
        mid_idx1 = (n - 1) // 2
        mid_idx2 = mid_idx1 + 1
        return [mid_idx1, mid_idx2]
    else:
        mid_idx = n // 2
        return mid_idx
if __name__ == '__main__':
    test_cases = [
        [],                                      
        ['a'],                                             
        [1, 2],                                           
        [1, 2, 3],                                         
        [0, 1, 2, 3, 4]                                   
    ]
    for i in range(len(test_cases)):
        data = test_cases[i]
        result = find_middle_index(data)
        if isinstance(result, list):
            print(f"Input: {data}, Middle indices: {result}")
        else:
            print(f"Input: {data}, Middle index: {result}")