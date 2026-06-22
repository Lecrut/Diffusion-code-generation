def compare_lists(list_a, list_b):
    results = []
    for a, b in zip(list_a, list_b):
        if a > b:
            results.append(f"{a} > {b}")
    return results

if __name__ == '__main__':
    list_a = [5, 3, 8, 2]
    list_b = [4, 6, 7, 1]
    output = compare_lists(list_a, list_b)
    for msg in output:
        print(msg)