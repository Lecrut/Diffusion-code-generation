def compare_and_report(list1, list2):
    if not all(isinstance(x, int) for x in list1 + list2):
        raise ValueError("All elements in both lists must be integers.")
    
    sum1 = sum(list1)
    sum2 = sum(list2)
    
    results = {
        "sum1": sum1,
        "sum2": sum2,
        "winner": None
    }
    
    if sum1 > sum2:
        results["winner"] = list1
    elif sum2 > sum1:
        results["winner"] = list2
    
    return (results["sum1"], results["sum2"], results["winner"])

if __name__ == '__main__':
    list_a = [10, 20, 30]
    list_b = [15, 25, 35]
    result = compare_and_report(list_a, list_b)
    print(result)