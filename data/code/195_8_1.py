from collections import Counter
def compare_lists_ignoring_order(list1, list2):
    freq1 = Counter(list1)
    freq2 = Counter(list2)
    return freq1 == freq2
if __name__ == '__main__':
    list_a = [1, 2, 2, 3]
    list_b = [3, 2, 1, 2]
    print(f"List A: {list_a}")
    print(f"List B: {list_b}")
    result1 = compare_lists_ignoring_order(list_a, list_b)
    print(f"Comparison result (A vs B): {result1}")
    list_c = [1, 2, 3]
    list_d = [1, 2, 4]
    print(f"\nList C: {list_c}")
    print(f"List D: {list_d}")
    result2 = compare_lists_ignoring_order(list_c, list_d)
    print(f"Comparison result (C vs D): {result2}")
    list_e = [1, 1, 2]
    list_f = [1, 2, 2]
    print(f"\nList E: {list_e}")
    print(f"List F: {list_f}")
    result3 = compare_lists_ignoring_order(list_e, list_f)
    print(f"Comparison result (E vs F): {result3}")
    list_g = [5, 5, 6]
    list_h = [5, 6, 6]
    print(f"\nList G: {list_g}")
    print(f"List H: {list_h}")
    result4 = compare_lists_ignoring_order(list_g, list_h)
    print(f"Comparison result (G vs H): {result4}")