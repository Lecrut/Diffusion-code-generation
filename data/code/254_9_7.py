def second_smallest(lst):
    if len(lst) < 2:
        return None
    first, second = float('inf'), float('inf')
    for num in lst:
        if num <= first:
            first, second = num, first
        elif num < second:
            second = num
    return second if second != float('inf') else first

if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print(second_smallest(sample_list))