def find_middle_element(lst):
    if not lst:
        raise ValueError('The list is empty')
    middle_index = len(lst) // 2
    return lst[middle_index]

if __name__ == '__main__':
    odd_numbers = [1, 3, 5, 7, 9]
    even_numbers = [2, 4, 6, 8, 10, 12]
    
    print(find_middle_element(odd_numbers))
    print(find_middle_element(even_numbers))