def find_longest_differing_subsequence(list1, list2):
    n = len(list1)
    m = len(list2)
    if n == 0 or m == 0:
        return ([], [], -1)
    max_len = -1
    longest_subsequence1 = []
    longest_subsequence2 = []
    for i in range(n):
        for j in range(i, n):
            sub1 = list1[i:j+1]
            sub2 = list2[i:j+1]
            if len(sub1) != len(sub2):
                continue
            if sub1 != sub2:
                current_len = len(sub1)
                if current_len > max_len:
                    max_len = current_len
                    longest_subsequence1 = sub1
                    longest_subsequence2 = sub2
    if max_len == -1:
        return ([], [], 0)
    else:
        return (longest_subsequence1, longest_subsequence2, max_len)
if __name__ == '__main__':
    list_a = [1, 2, 3, 4, 5]
    list_b = [1, 2, 3, 6, 5]
    result_a, result_b, length = find_longest_differing_subsequence(list_a, list_b)
    print(f"List A: {list_a}")
    print(f"List B: {list_b}")
    print(f"Longest differing subsequence from A: {result_a}")
    print(f"Longest differing subsequence from B: {result_b}")
    print(f"Length of longest differing subsequence: {length}")
    list_c = [1, 1, 2, 3, 4]
    list_d = [1, 1, 5, 6, 7]
    result_c, result_d, length = find_longest_differing_subsequence(list_c, list_d)
    print(f"\nList C: {list_c}")
    print(f"List D: {list_d}")
    print(f"Longest differing subsequence from C: {result_c}")
    print(f"Longest differing subsequence from D: {result_d}")
    print(f"Length of longest differing subsequence: {length}")
    list_e = [1, 2, 3]
    list_f = [4, 5, 6]
    result_e, result_f, length = find_longest_differing_subsequence(list_e, list_f)
    print(f"\nList E: {list_e}")
    print(f"List F: {list_f}")
    print(f"Longest differing subsequence from E: {result_e}")
    print(f"Longest differing subsequence from F: {result_f}")
    print(f"Length of longest differing subsequence: {length}")