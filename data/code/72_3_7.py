def compare_lists(list_a, list_b):
    results = []
    min_length = min(len(list_a), len(list_b))
    for i in range(min_length):
        if list_a[i] > list_b[i]:
            results.append((list_a[i], list_b[i]))
    return results

if __name__ == '__main__':
    list_a = [10, 5, 8, 3]
    list_b = [2, 6, 9, 1]
    result = compare_lists(list_a, list_b)
    for first, second in result:
        print(f"{first} > {second}")