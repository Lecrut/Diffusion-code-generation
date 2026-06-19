def sum_of_differences(list1, list2):
    min_length = min(len(list1), len(list2))
    differences = [abs(a - b) for a, b in zip(list1[:min_length], list2[:min_length])]
    return sum(differences)

if __name__ == '__main__':
    sample_list1 = [5, 10, 15, 20]
    sample_list2 = [3, 8, 12, 18]
    result = sum_of_differences(sample_list1, sample_list2)
    print(result)