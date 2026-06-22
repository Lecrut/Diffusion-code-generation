def reverse_list(lst):
    def swap_elements(i, j):
        lst[i], lst[j] = lst[j], lst[i]
    
    length = len(lst)
    mid_point = length // 2
    
    for i in range(mid_point):
        swap_elements(i, length - i - 1)
    
    return lst

if __name__ == '__main__':
    sample_list = [7, 8, 9, 10, 11]
    reversed_list = reverse_list(sample_list)
    print(reversed_list)