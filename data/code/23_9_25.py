def compare_and_report(list1, list2):
    sum1 = sum(list1)
    sum2 = sum(list2)
    
    if sum1 > sum2:
        return sum1, list1
    else:
        return sum2, list2

if __name__ == '__main__':
    list_a = [10, 20, 30]
    list_b = [5, 15, 25, 35]
    
    result_sum, winning_list = compare_and_report(list_a, list_b)
    print(f"Sum: {result_sum}, Winning List: {winning_list}")