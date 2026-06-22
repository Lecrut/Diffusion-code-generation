import random

def find_middle_value(numbers):
    if not numbers:
        raise ValueError("List must not be empty")
    
    n = len(numbers)
    if n % 2 == 1:
        return _select_kth(numbers, n // 2)
    else:
        left = _select_kth(numbers, n // 2 - 1)
        right = _select_kth(numbers, n // 2)
        return (left + right) / 2

def _select_kth(lst, k):
    if len(lst) == 1:
        return lst[0]
    
    pivot = lst[len(lst) // 2]
    lows = [x for x in lst if x < pivot]
    highs = [x for x in lst if x > pivot]
    pivots = [x for x in lst if x == pivot]
    
    if k < len(lows):
        return _select_kth(lows, k)
    elif k < len(lows) + len(pivots):
        return pivots[0]
    else:
        return _select_kth(highs, k - len(lows) - len(pivots))

if __name__ == '__main__':
    sample_list = [7, 1, 3, 4, 6, 5, 2]
    result = find_middle_value(sample_list)
    print(result)