def compute_differences(list1, list2):
    differences = {}
    length_difference = min(len(list1), len(list2))
    for i in range(length_difference):
        differences[i] = list1[i] - list2[i]
    return differences

if __name__ == '__main__':
    list_a = [15, 25, 35, 45]
    list_b = [5, 10, 15, 20]
    result_dict = compute_differences(list_a, list_b)
    print(result_dict)