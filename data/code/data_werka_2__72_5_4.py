def compare_elements(a, b):
    if a > b:
        return 'A > B'
    if a < b:
        return 'A < B'
    return 'A == B'

def compare_lists(list_a, list_b):
    min_len = min(len(list_a), len(list_b))
    for i in range(min_len):
        yield compare_elements(list_a[i], list_b[i])

if __name__ == '__main__':
    list_a = [10, 20, 30]
    list_b = [10, 15, 35, 40]
    results = list(compare_lists(list_a, list_b))
    print(results)