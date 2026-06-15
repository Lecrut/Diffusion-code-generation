def find_combined_maximum(list1, list2):
    combined = list1 + list2
    if not combined:
        raise ValueError("Both lists are empty")
    return max(combined)
if __name__ == '__main__':
    list_a = [10, 5, 20, 3]
    list_b = [15, 8, 25, 1]
    result = find_combined_maximum(list_a, list_b)
    print(result)