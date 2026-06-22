def find_middle_element(lst):
    if not lst:
        raise ValueError('The list is empty')
    middle_index = len(lst) // 2
    return lst[middle_index]

if __name__ == '__main__':
    sample_data = {
        'odd_list': [1, 3, 5, 7, 9],
        'even_list': [2, 4, 6, 8, 10, 12]
    }
    
    for key, lst in sample_data.items():
        print(f"The middle element of {key} is: {find_middle_element(lst)}")