def compare_pair(a, b):
    if a > b:
        return 'A > B'
    if a < b:
        return 'A < B'
    return 'A == B'

def compare_lists(list_a, list_b):
    min_len = min(len(list_a), len(list_b))
    for i in range(min_len):
        yield compare_pair(list_a[i], list_b[i])

if __name__ == '__main__':
    list_a = [10, 5, 20, 15]
    list_b = [12, 5, 10, 20, 30]
    results = list(compare_lists(list_a, list_b))
    print(results)