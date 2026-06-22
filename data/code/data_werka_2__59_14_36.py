def find_middle_item(lst):
    if not lst:
        raise ValueError('The list is empty')
    
    length = len(lst)
    middle_index = length // 2
    
    if length % 2 == 0:
        return (lst[middle_index - 1] + lst[middle_index]) / 2
    else:
        return lst[middle_index]

if __name__ == '__main__':
    sample_list_odd = [10, 20, 30, 40, 50]
    sample_list_even = [5, 15, 25, 35, 45, 55]
    
    print(find_middle_item(sample_list_odd))
    print(find_middle_item(sample_list_even))