def find_longest_differing_subsequence(list1, list2):
    n = len(list1)
    m = len(list2)
    if n == 0 or m == 0:
        return {"length": 0, "subsequence1": [], "subsequence2": []}
    max_len = 0
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
    return {
        "length": max_len,
        "subsequence1": longest_subsequence1,
        "subsequence2": longest_subsequence2
    }
if __name__ == '__main__':
    list_a = [1, 2, 3, 4, 5, 6]
    list_b = [1, 2, 3, 8, 5, 6]
    report1 = find_longest_differing_subsequence(list_a, list_b)
    print("--- Test Case 1 ---")
    print(f"List A: {list_a}")
    print(f"List B: {list_b}")
    print(f"Report: {report1}")
    list_c = [10, 20, 30, 40]
    list_d = [11, 22, 33, 44]
    report2 = find_longest_differing_subsequence(list_c, list_d)
    print("\n--- Test Case 2 ---")
    print(f"List C: {list_c}")
    print(f"List D: {list_d}")
    print(f"Report: {report2}")
    list_e = [1, 1, 1, 1]
    list_f = [2, 2, 2, 2]
    report3 = find_longest_differing_subsequence(list_e, list_f)
    print("\n--- Test Case 3 ---")
    print(f"List E: {list_e}")
    print(f"List F: {list_f}")
    print(f"Report: {report3}")
    list_g = [1, 2, 3]
    list_h = [4, 5, 6]
    report4 = find_longest_differing_subsequence(list_g, list_h)
    print("\n--- Test Case 4 ---")
    print(f"List G: {list_g}")
    print(f"List H: {list_h}")
    print(f"Report: {report4}")