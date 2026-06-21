def compare_elements(list_a, list_b):
    results = []
    for x, y in zip(list_a, list_b):
        if x < y:
            results.append((x, y, "less"))
        elif x > y:
            results.append((x, y, "greater"))
        else:
            results.append((x, y, "equal"))
    return results

if __name__ == '__main__':
    first_list = [10, 20, 30]
    second_list = [10, 15, 35]
    comparison_results = compare_elements(first_list, second_list)
    print(comparison_results)