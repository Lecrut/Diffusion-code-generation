def find_median(data):
    n = len(data)
    if n == 0:
        raise ValueError("Input list is empty")
    
    if n % 2 == 1:
        return select_kth(data, n // 2)
    else:
        lower_middle_index = n // 2 - 1
        upper_middle_index = n // 2
        return (select_kth(data, lower_middle_index) + select_kth(data, upper_middle_index)) / 2.0

def select_kth(data, k):
    if len(data) == 1:
        return data[0]
    
    pivot = data[len(data) // 2]
    lows = [x for x in data if x < pivot]
    highs = [x for x in data if x > pivot]
    pivots = [x for x in data if x == pivot]
    
    if k < len(lows):
        return select_kth(lows, k)
    elif k < len(lows) + len(pivots):
        return pivots[0]
    else:
        return select_kth(highs, k - len(lows) - len(pivots))

if __name__ == '__main__':
    list1 = [5, 2, 8, 1, 9]
    print(find_median(list1))
    
    list2 = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    print(find_median(list2))