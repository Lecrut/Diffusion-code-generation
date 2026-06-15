def compare_min_max(list1, list2):
    min1 = min(list1)
    max1 = max(list1)
    min2 = min(list2)
    max2 = max(list2)
    return {
        "list1": {"min": min1, "max": max1},
        "list2": {"min": min2, "max": max2}
    }
if __name__ == '__main__':
    list_a = [1, 5, 2, 8, 3]
    list_b = [10, 4, 15, 6, 9]
    result = compare_min_max(list_a, list_b)
    print(f"List A: {list_a}")
    print(f"List B: {list_b}")
    print(f"Result: {result}")