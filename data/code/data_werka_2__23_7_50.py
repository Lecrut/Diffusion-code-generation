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
    list_a = [3, 6, 9]
    list_b = [1, 4, 7, 10]
    result = compare_and_report(list_a, list_b)
    print(result)