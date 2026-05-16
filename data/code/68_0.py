def calculate_difference_sum(list1, list2):
    min_length = min(len(list1), len(list2))
    difference_sum = 0
    for i in range(min_length):
        difference_sum += list1[i] - list2[i]
    return difference_sum
if __name__ == '__main__':
    list_a = [1, 2, 3, 4, 5]
    list_b = [10, 20, 30, 40]
    result = calculate_difference_sum(list_a, list_b)
    print(result)