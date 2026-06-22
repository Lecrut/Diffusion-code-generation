def compare_and_report(list1, list2):
    def calculate_sum(lst):
        return sum(lst)
    
    sum1 = calculate_sum(list1)
    sum2 = calculate_sum(list2)
    
    if sum1 > sum2:
        return sum1, list1
    elif sum2 > sum1:
        return sum2, list2
    else:
        return sum1, None

if __name__ == '__main__':
    LIST_A = [10, 20, 30, 40]
    LIST_B = [5, 15, 25, 35, 45]
    
    result = compare_and_report(LIST_A, LIST_B)
    print(result)