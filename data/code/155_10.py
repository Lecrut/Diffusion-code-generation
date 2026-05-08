def calculate_list_sum(numbers):
    return sum(numbers)
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    result1 = calculate_list_sum(list1)
    print(result1)
    list2 = [10.5, 20.5, 30.0]
    result2 = calculate_list_sum(list2)
    print(result2)
    list3 = [-1, 5, -3, 10]
    result3 = calculate_list_sum(list3)
    print(result3)