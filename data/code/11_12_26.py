def calculate_length_ratio(list1, list2):
    length1 = len(list1)
    length2 = len(list2)
    if length2 == 0:
        return float('inf')
    return length1 / length2
if __name__ == '__main__':
    list_a = [1, 2, 3, 4, 5]
    list_b = [6, 7, 8]
    ratio = calculate_length_ratio(list_a, list_b)
    print(ratio)