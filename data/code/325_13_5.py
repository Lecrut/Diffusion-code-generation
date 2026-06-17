def compare_list_sums(list1, list2):
    sum1 = sum(list1)
    sum2 = sum(list2)
    print(f"Sum of the first list: {sum1}")
    print(f"Sum of the second list: {sum2}")
    if sum1 > sum2:
        print("The sum of the first list is greater than the sum of the second list.")
    elif sum1 < sum2:
        print("The sum of the first list is less than the sum of the second list.")
    else:
        print("The sums of the two lists are equal.")
if __name__ == '__main__':
    list_a = [1, 5, 10, 2]
    list_b = [3, 7, 4, 6]
    compare_list_sums(list_a, list_b)