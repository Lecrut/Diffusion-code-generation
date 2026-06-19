IS_FIRST_GREATER = lambda lst: lst[0] > lst[1]

if __name__ == '__main__':
    sample_list_1 = [10, 5]
    print(IS_FIRST_GREATER(sample_list_1))
    
    sample_list_2 = [3, 7]
    print(IS_FIRST_GREATER(sample_list_2))
    
    sample_list_3 = [7.5, 7.5]
    print(IS_FIRST_GREATER(sample_list_3))
    
    sample_list_4 = [-2, -5]
    print(IS_FIRST_GREATER(sample_list_4))