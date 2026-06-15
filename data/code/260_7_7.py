import math
def calculate_median(data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    if n == 0:
        return None
    if n % 2 == 1:
        return sorted_data[n // 2]
    else:
        mid1 = sorted_data[n // 2 - 1]
        mid2 = sorted_data[n // 2]
        return (mid1 + mid2) / 2
def compare_lists(list1, list2):
    median1 = calculate_median(list1)
    median2 = calculate_median(list2)
    if median1 is None and median2 is None:
        return None
    if median1 is None:
        return list2
    if median2 is None:
        return list1
    if median1 >= median2:
        return list1
    else:
        return list2
if __name__ == '__main__':
    list_a = [1, 3, 5, 7, 9]
    list_b = [2, 4, 6, 8, 10]
    result1 = compare_lists(list_a, list_b)
    print(f"List A: {list_a}, Median: {calculate_median(list_a)}")
    print(f"List B: {list_b}, Median: {calculate_median(list_b)}")
    print(f"Result (A vs B): {result1}\n")
    list_c = [10, 20, 30]
    list_d = [5, 15, 25]
    result2 = compare_lists(list_c, list_d)
    print(f"List C: {list_c}, Median: {calculate_median(list_c)}")
    print(f"List D: {list_d}, Median: {calculate_median(list_d)}")
    print(f"Result (C vs D): {result2}\n")
    list_e = [1, 2, 3, 4]
    list_f = [5, 6, 7, 8]
    result3 = compare_lists(list_e, list_f)
    print(f"List E: {list_e}, Median: {calculate_median(list_e)}")
    print(f"List F: {list_f}, Median: {calculate_median(list_f)}")
    print(f"Result (E vs F): {result3}\n")
    list_g = [1, 2]
    list_h = [10, 20]
    result4 = compare_lists(list_g, list_h)
    print(f"List G: {list_g}, Median: {calculate_median(list_g)}")
    print(f"List H: {list_h}, Median: {calculate_median(list_h)}")
    print(f"Result (G vs H): {result4}\n")