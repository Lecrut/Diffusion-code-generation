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
    report = find_longest_differing_subsequence(list_a, list_b)
    print(report)
    list_c = [1, 1, 1, 1, 1]
    list_d = [0, 0, 0, 0, 0]
    report2 = find_longest_differing_subsequence(list_c, list_d)
    print(report2)
    list_e = [1, 2, 3]
    list_f = [4, 5, 6]
    report3 = find_longest_differing_subsequence(list_e, list_f)
    print(report3)
    list_g = [1, 2, 3, 4]
    list_h = [1, 2, 3, 4]
    report4 = find_longest_differing_subsequence(list_g, list_h)
    print(report4)