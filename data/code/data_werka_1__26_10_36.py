is_greater = lambda lst: lst[0] > lst[1]
if __name__ == '__main__':
    list_one = [8, 3]
    result_one = is_greater(list_one)
    print(f"is_greater({list_one}): {result_one}")
    
    list_two = [2.5, 4.7]
    result_two = is_greater(list_two)
    print(f"is_greater({list_two}): {result_two}")
    
    list_three = [-10, -20]
    result_three = is_greater(list_three)
    print(f"is_greater({list_three}): {result_three}")