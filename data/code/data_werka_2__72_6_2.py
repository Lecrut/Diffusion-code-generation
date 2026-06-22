def compare_lists(list1, list2):
    results = []
    for a, b in zip(list1, list2):
        if a < b:
            results.append((a, b, "less than"))
        elif a > b:
            results.append((a, b, "greater than"))
        else:
            results.append((a, b, "equal to"))
    return results

if __name__ == '__main__':
    list_a = [1, 5, 3, 8]
    list_b = [2, 5, 1, 8]
    output = compare_lists(list_a, list_b)
    print(output)