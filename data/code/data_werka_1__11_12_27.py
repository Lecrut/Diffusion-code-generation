def calculate_length_ratio(list1, list2):
    return len(list1) / len(list2) if len(list2) != 0 else float('inf')

if __name__ == '__main__':
    list_a = [1, 2, 3, 4, 5]
    list_b = [6, 7, 8]
    ratio = calculate_length_ratio(list_a, list_b)
    print(ratio)