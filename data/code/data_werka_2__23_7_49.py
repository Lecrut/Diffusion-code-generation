def compare_and_report(list1, list2):
    sum1 = sum(list1)
    sum2 = sum(list2)
    
    if sum1 > sum2:
        winning_list = list1
    elif sum2 > sum1:
        winning_list = list2
    else:
        return sum1, None
    
    return sum1 if sum1 > sum2 else sum2, winning_list

if __name__ == '__main__':
    list_a = [10, 20, 30, 40]
    list_b = [5, 15, 25, 35, 45]
    result = compare_and_report(list_a, list_b)
    print(result)