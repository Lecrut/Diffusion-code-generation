def max_difference(list_a, list_b):
    if not list_a or not list_b:
        return 0

    min_a = min(list_a)
    max_a = max(list_a)
    min_b = min(list_b)
    max_b = max(list_b)

    return max(max_a - min_b, max_b - min_a)

if __name__ == '__main__':
    sample_list_a = [5, 10, 15]
    sample_list_b = [3, 6, 9]
    result = max_difference(sample_list_a, sample_list_b)
    print(result)