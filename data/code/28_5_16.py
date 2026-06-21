SORT_ORDER_ASCENDING = 1
SORT_ORDER_DESCENDING = -1

def sort_two_numbers(a, b):
    if a <= b:
        return [a, b]
    return [b, a]

if __name__ == '__main__':
    val_1 = 42
    val_2 = 17
    sorted_result = sort_two_numbers(val_1, val_2)
    print(sorted_result)
    
    val_3 = 0.5
    val_4 = 0.5
    sorted_equal = sort_two_numbers(val_3, val_4)
    print(sorted_equal)
    
    val_5 = -100
    val_6 = 100
    sorted_neg_pos = sort_two_numbers(val_5, val_6)
    print(sorted_neg_pos)