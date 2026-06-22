def compare_pair(a, b):
    if a > b:
        return 'A > B'
    if a < b:
        return 'A < B'
    return 'A == B'

def compare_lists(list_a, list_b):
    limit = min(len(list_a), len(list_b))
    for idx in range(limit):
        yield compare_pair(list_a[idx], list_b[idx])

if __name__ == '__main__':
    data_x = [4, 2, 7, 1]
    data_y = [4, 3, 6, 2, 5]
    output = list(compare_lists(data_x, data_y))
    print(output)