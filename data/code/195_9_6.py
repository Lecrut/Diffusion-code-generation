def find_longest_differing_subsequence(list1, list2):
    n = len(list1)
    m = len(list2)
    if n == 0 or m == 0:
        return []
    longest_diff = []
    max_length = 0
    for i in range(n):
        for j in range(i, n):
            sub1 = list1[i:j+1]
            sub2 = list2[i:j+1]
            if len(sub1) != len(sub2):
                continue
            if sub1 != sub2:
                current_length = len(sub1)
                if current_length > max_length:
                    max_length = current_length
                    longest_diff = sub1
                elif current_length == max_length:
                    pass
    return longest_diff
if __name__ == '__main__':
    list_a = [1, 2, 3, 4, 5, 6]
    list_b = [1, 2, 3, 8, 5, 6]
    result1 = find_longest_differing_subsequence(list_a, list_b)
    print("List A:", list_a)
    print("List B:", list_b)
    print("Longest differing subsequence:")
    print(result1)
    list_c = [10, 20, 30, 40, 50]
    list_d = [10, 20, 30, 99, 50]
    result2 = find_longest_differing_subsequence(list_c, list_d)
    print("\nList C:", list_c)
    print("List D:", list_d)
    print("Longest differing subsequence:")
    print(result2)
    list_e = [1, 1, 1, 1, 1]
    list_f = [2, 2, 2, 2, 2]
    result3 = find_longest_differing_subsequence(list_e, list_f)
    print("\nList E:", list_e)
    print("List F:", list_f)
    print("Longest differing subsequence:")
    print(result3)
    list_g = [1, 2, 3]
    list_h = [4, 5, 6]
    result4 = find_longest_differing_subsequence(list_g, list_h)
    print("\nList G:", list_g)
    print("List H:", list_h)
    print("Longest differing subsequence:")
    print(result4)