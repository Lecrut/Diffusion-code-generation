def compare_and_report(list1, list2):
    sum1 = sum(list1)
    sum2 = sum(list2)
    
    results = {
        'sum1': sum1,
        'sum2': sum2,
        'winning_list': None
    }
    
    if sum1 > sum2:
        results['winning_list'] = list1
    elif sum2 > sum1:
        results['winning_list'] = list2
    
    return results

if __name__ == '__main__':
    list_a = [10, 20, 30]
    list_b = [5, 5, 5, 50]
    result = compare_and_report(list_a, list_b)
    print(result)