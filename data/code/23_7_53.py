def compare_and_report(list1, list2):
    sum1 = sum(list1)
    sum2 = sum(list2)
    
    if sum1 > sum2:
        return sum1, list1
    elif sum2 > sum1:
        return sum2, list2
    else:
        return sum1, []

if __name__ == '__main__':
    list_a = [1, 2, 3, 4, 5]
    list_b = [3, 4, 5, 6]
    
    result_sum, winning_list = compare_and_report(list_a, list_b)
    print("Sum:", result_sum)
    print("Winning List:", winning_list)