def compute_difference_sum(list1, list2):
    min_length = min(len(list1), len(list2))
    if not min_length:
        return 0
    differences = (a - b for a, b in zip(list1[:min_length], list2[:min_length]))
    return sum(differences)

if __name__ == '__main__':
    sample_list1 = [3, 6, 9, 12]
    sample_list2 = [1, 4, 7]
    result = compute_difference_sum(sample_list1, sample_list2)
    print(result)