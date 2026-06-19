def calculate_length_ratio(list1, list2):
    len1 = len(list1)
    len2 = len(list2)
    if len2 == 0:
        return float('inf') if len1 != 0 else 0.0
    return len1 / len2

if __name__ == '__main__':
    list_a = [1, 2, 3, 4, 5]
    list_b = [6, 7, 8]
    ratio = calculate_length_ratio(list_a, list_b)
    print(ratio)