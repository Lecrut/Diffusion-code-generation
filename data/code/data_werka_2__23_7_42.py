def compare_and_report(list1, list2):
    if not all(isinstance(x, int) for x in list1 + list2):
        raise ValueError("All elements in both lists must be integers.")
    
    sum1 = sum(list1)
    sum2 = sum(list2)
    
    if sum1 > sum2:
        return sum1, list1
    elif sum2 > sum1:
        return sum2, list2
    else:
        return sum1, None

if __name__ == '__main__':
    list_a = [7, 8, 9]
    list_b = [3, 4, 5, 6]
    result = compare_and_report(list_a, list_b)
    print(result)