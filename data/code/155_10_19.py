def calculate_list_sum(numbers):
    return sum(numbers)

if __name__ == '__main__':
    list1 = [2, 4, 6, 8, 10]
    result1 = calculate_list_sum(list1)
    print(result1)
    
    list2 = [5.5, 7.5, 9.0]
    result2 = calculate_list_sum(list2)
    print(result2)
    
    list3 = [-2, -4, 6, 8, -10]
    result3 = calculate_list_sum(list3)
    print(result3)