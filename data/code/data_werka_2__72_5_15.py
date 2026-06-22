def compare_pair(a, b):
    if a > b:
        return 'A > B'
    if a < b:
        return 'A < B'
    return 'A == B'

def compare_lists(list_a, list_b):
    if not isinstance(list_a, (list, tuple)):
        raise ValueError("list_a must be a list or tuple")
    if not isinstance(list_b, (list, tuple)):
        raise ValueError("list_b must be a list or tuple")
    
    length_a = len(list_a)
    length_b = len(list_b)
    limit = length_a if length_a < length_b else length_b
    
    for i in range(limit):
        yield compare_pair(list_a[i], list_b[i])

if __name__ == '__main__':
    sample_a = [10, 20, 30]
    sample_b = [10, 15, 35, 40]
    results = list(compare_lists(sample_a, sample_b))
    print(results)